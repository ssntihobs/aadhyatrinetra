from wagtail.models import Site

from categories.models import Category
from .models import BlogPage


def categories(request):
    categories = Category.objects.filter(parent__isnull=True)
    context = {
        'categories': categories
    }

    return context


def blog_page(request):
    wagtail_site = Site.find_for_request(request)
    context = {
        'blog_page': BlogPage.objects.in_site(wagtail_site).first()
    }
    return context
