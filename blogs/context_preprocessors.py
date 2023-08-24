from wagtail.models import Site
from .models import BlogPage


def blog_page(request):
    wagtail_site = Site.find_for_request(request)
    context = {
        'blog_page': BlogPage.objects.in_site(wagtail_site).first()
    }
    return context
