# # fields.py
#
# from wagtail.blocks import RichTextBlock
#
# class CustomRichTextBlock(RichTextBlock):
#     def __init__(self, required=True, help_text=None, editor='default', features=None, **kwargs):
#         super().__init__(**kwargs)
#         self.features = features
#
#     def prepare_value(self, value):
#         value = super().prepare_value(value)
#         for feature in self.features:
#             value = value.replace(f'<{feature}>', f'<{feature} class="{self.get_class_for_element(feature)}">')
#         return value
#
#     def get_class_for_element(self, element):
#         # Define the custom classes for different elements here
#         custom_classes = {
#             'h1': 'text-5xl',
#             'h2': 'text-4xl',
#             'h3': 'text-3xl',
#             'h4': 'text-2xl',
#             'h5': 'text-xl',
#             'h6': 'text-lg',
#             'p': 'text-base',
#             # Add more elements and classes as needed
#         }
#         return custom_classes.get(element, '')
