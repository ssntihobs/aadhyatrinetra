from django.db import models
from wagtail.snippets.models import register_snippet


@register_snippet
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
