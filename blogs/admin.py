from django.contrib import admin
from .models import FeaturedPost
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet


class FeaturedPostViewSet(SnippetViewSet):
    model = FeaturedPost
    list_display = ("post",)


register_snippet(FeaturedPostViewSet)
