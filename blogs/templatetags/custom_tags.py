from datetime import datetime

from django.template import Library
from django.template.defaultfilters import truncatechars
from django.utils import timezone
from django.utils.timesince import timesince

register = Library()


@register.simple_tag()
def post_page_slug_url(post_page, blog_page):
    url = post_page.full_url
    return url

@register.filter
def truncate_with_ellipsis(text, limit):
    return truncatechars(text, limit) if len(text) > limit else text

# @register.simple_tag()
# def blog_page_category_pagination_url(page_num, blog_page):
#     url = blog_page.reverse_subpage(
#         "paginated_view",
#         args=(
#             page_num,
#         ),
#     )
#     return url