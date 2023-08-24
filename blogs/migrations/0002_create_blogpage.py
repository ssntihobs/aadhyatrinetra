# -*- coding: utf-8 -*-
from django.db import migrations


def create_blogpage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    Page = apps.get_model("wagtailcore.Page")
    Site = apps.get_model("wagtailcore.Site")
    BlogPage = apps.get_model("blogs.BlogPage")

    # Delete the default homepage
    # If migration is run multiple times, it may have already been deleted
    Page.objects.filter(id=2).delete()

    # Create content type for homepage model
    blogpage_content_type, __ = ContentType.objects.get_or_create(
        model="blogpage", app_label="blogs"
    )

    # Create a new homepage
    blogpage = BlogPage.objects.create(
        title="Topic",
        draft_title="Topic",
        slug="topic",
        content_type=blogpage_content_type,
        path="00010001",
        depth=2,
        numchild=0,
        url_path="/topic/",
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(hostname="localhost", root_page=blogpage, is_default_site=True)


def remove_blogpage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    HomePage = apps.get_model("blogs.BlogPage")

    # Delete the default homepage
    # Page and Site objects CASCADE
    HomePage.objects.filter(slug="blog", depth=2).delete()

    # Delete content type for homepage model
    ContentType.objects.filter(model="blogpage", app_label="blogs").delete()


class Migration(migrations.Migration):
    run_before = [
        ("wagtailcore", "0053_locale_model"),
    ]

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_blogpage, remove_blogpage),
    ]
