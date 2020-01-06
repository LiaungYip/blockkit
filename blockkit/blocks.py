from . import Text
from .components import Component
from .elements import Element, SelectBase, Button, Overflow, DatePicker
from .fields import ArrayField, ObjectField, StringField, TextField, UrlField


class Block(Component):
    type = StringField()
    block_id = StringField(max_length=255)


class Section(Block):
    text = TextField(max_length=3000)
    fields = ArrayField(Text, max_items=10)
    accessory = ObjectField(Element)

    def __init__(self, text, block_id=None, fields=None, accessory=None):
        super().__init__("section", block_id, text, fields, accessory)


class Divider(Block):
    def __init__(self, block_id=None):
        super().__init__("divider", block_id)


class ImageBlock(Block):
    image_url = UrlField(max_length=3000)
    alt_text = StringField(max_length=2000)
    title = TextField(plain=True, max_length=2000)

    def __init__(self, image_url, alt_text, title=None, block_id=None):
        super().__init__("image", block_id, image_url, alt_text, title)


class Actions(Block):
    elements = ArrayField(SelectBase, Button, Overflow, DatePicker, max_items=5)

    def __init__(self, elements, block_id=None):
        super().__init__("actions", block_id, elements)
