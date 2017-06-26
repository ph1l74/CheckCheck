import tesserocr
from PIL import Image
from io import BytesIO

print(tesserocr.get_languages())


def image_to_text(images):
    text = []
    for image in images:
        image_object = Image.open(image[0])
        text.append(tesserocr.image_to_text(image_object, 'rus'))
    return text
