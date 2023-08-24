from wagtail.blocks import StructBlock, BooleanBlock, RichTextBlock, ListBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailmarkdown.blocks import MarkdownBlock


class ImageText(StructBlock):
    reverse = BooleanBlock(required=False)
    text = RichTextBlock()
    image = ImageChooserBlock()


class BodyBlock(StreamBlock):
    markdown = MarkdownBlock(icon="code")

    image_text = ImageText()
    carousel = ListBlock(ImageChooserBlock())
    gallery = ListBlock(ImageChooserBlock())
