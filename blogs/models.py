import math

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.http import Http404
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.text import slugify
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, route
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtailmetadata.models import MetadataPageMixin
from wagtail.images.models import Image, AbstractImage, AbstractRendition
import datetime
from django.contrib.auth import get_user_model
from taggit.models import Tag as TaggitTag, TaggedItemBase
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

from blogs.blocks import BodyBlock
from categories.models import Category

User = get_user_model()


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True


# @register_setting
# class ExtraTags(BaseSiteSetting):
#     fb_app_id = models.CharField(max_length=20)
#     fb_pages = models.CharField(max_length=128)


class CustomImage(AbstractImage):
    admin_form_fields = Image.admin_form_fields + (
        'file',
    )

    def get_upload_to(self, filename):
        current_date = datetime.date.today()
        return f'images/{current_date.year}/{current_date.strftime("%m")}/{filename}'


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(CustomImage, on_delete=models.CASCADE, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )

    def get_upload_to(self, filename):
        current_date = datetime.date.today()
        return f'images/{current_date.year}/{current_date.strftime("%m")}/{filename}'


class CustomPageForm(WagtailAdminPageForm):
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        slug = cleaned_data.get('slug')

        if title and not slug:
            cleaned_data['slug'] = slugify(title)

        return cleaned_data


class BlogPage(MetadataPageMixin, RoutablePageMixin, Page):
    base_form_class = CustomPageForm
    posts = []
    category = None

    def get_context(self, request, *args, **kwargs):
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        context['posts'] = self.get_paginated_posts(request, self.posts)
        context['pop_posts'] = self.get_random_posts()

        if 'topic' in request.path or 'tag' in request.path:
            category = Category.objects.get(slug=self.filter_term)
            context['featured_posts'] = self.get_featured_posts(category)
            context['page'].title = self.filter_term.capitalize()
        else:
            context['page'].title = 'ImpelVerse'
            context['page'].description = 'We are here to guide you.'
            context['featured_posts'] = self.get_featured_posts()
        return context

    def get_random_posts(self):
        return BlogPost.objects.order_by('?')[:5]

    def get_featured_posts(self, category=None):
        if category:
            return FeaturedPost.objects.filter(post__category=category)
        return FeaturedPost.objects.all()

    def get_posts(self):
        return BlogPost.objects.live().specific().order_by("first_published_at").prefetch_related('thumbnail',
                                                                                                  'category', 'owner')

    def get_paginated_posts(self, request, qs):
        paginator = Paginator(qs, 10)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.object_list.none()

        return posts

    @path('')
    def post_list(self, request, *args, **kwargs):
        self.posts = self.get_posts()
        return self.render(request)

    @path("<str:post_slug>")
    def post_page_by_slug(self, request, post_slug, *args, **kwargs):
        post_page = self.get_posts().filter(slug=post_slug).first()
        # if not post_page:
        #     raise Http404
        return post_page.serve(request)

    @path('topic/<str:category>/')
    def post_by_category(self, request, category):
        self.filter_type = 'category'
        self.filter_term = category
        self.posts = self.get_posts().filter(category__slug=category)
        # if not self.posts:
        #     raise Http404
        return self.render(request)

    @path('tag/<str:tag>/')
    def post_by_tag(self, request, tag, *args, **kwargs):
        self.filter_type = 'tag'
        self.filter_term = tag
        self.posts = self.get_posts().filter(tags__slug=tag)
        print(self.posts)
        return self.render(request)

    @path("<str:post_slug>")
    def post_page_by_slug(self, request, post_slug, *args, **kwargs):
        post_page = self.get_posts().filter(slug=post_slug).first()
        # if not post_page:
        #     raise Http404
        return post_page.serve(request)

    @route(r"^search/$")
    def post_search(self, request, *args, **kwargs):
        search_query = request.GET.get("q", None)
        self.posts = self.get_posts()
        print(self.posts)
        if search_query:
            self.filter_term = search_query
            self.filter_type = 'Search'
            self.posts = self.posts.search(search_query)
        return self.render(request)


class BlogPost(MetadataPageMixin, Page):
    base_form_class = CustomPageForm
    content = StreamField(BodyBlock, use_json_field=True)
    tags = ClusterTaggableManager(through="blogs.BlogPostTag", blank=True)
    publication_date = models.DateField()
    thumbnail = models.ForeignKey(
        'blogs.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='images'
    )
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='blogs')

    content_panels = Page.content_panels + [
        FieldPanel('thumbnail'),
        FieldPanel('category'),
        # FieldPanel('description'),
        FieldPanel('publication_date'),
        FieldPanel('content'),
        FieldPanel('tags'),
    ]

    @cached_property
    def blog_page(self):
        return self.get_parent().specific

    def get_author(self):
        if self.owner:
            return f"{self.owner.first_name} {self.owner.last_name}"
        return None

    @cached_property
    def canonical_url(self):
        from blogs.templatetags.custom_tags import post_page_slug_url

        blog_page = self.blog_page
        return post_page_slug_url(self, blog_page)

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.first_published_at

        if diff.days == 0 and 0 <= diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "s ago"
            else:
                return str(seconds) + "s ago"

        if diff.days == 0 and 60 <= diff.seconds < 3600:
            minutes = math.floor(diff.seconds / 60)

            if minutes == 1:
                return str(minutes) + "m ago"
            else:
                return str(minutes) + "m ago"

        if diff.days == 0 and 3600 <= diff.seconds < 86400:
            hours = math.floor(diff.seconds / 3600)

            if hours == 1:
                return str(hours) + "h ago"
            else:
                return str(hours) + "h ago"

        # 1 day to 30 days
        if 1 <= diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if 30 <= diff.days < 365:
            months = math.floor(diff.days / 30)

            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days / 365)

            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
    ]


class BlogPostTag(TaggedItemBase):
    content_object = ParentalKey("blogs.BlogPost", related_name="post_tags")


@register_snippet
class FeaturedPost(models.Model):
    post = models.ForeignKey('blogs.BlogPost', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post}"
