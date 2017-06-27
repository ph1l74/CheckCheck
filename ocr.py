import tesserocr
from PIL import Image


def image_to_text(image):
    text = []
    image_object = Image.open(image)
    text.append(tesserocr.image_to_text(image_object, 'rus'))
    return text
