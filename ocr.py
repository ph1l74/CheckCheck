import tesserocr
from PIL import Image
from io import BytesIO

print(tesserocr.get_languages())


def image_to_text(images):
    #image_data = images[0][1].read()
    image_object = Image.open(images)
    text = tesserocr.image_to_text(image_object, 'rus')
    return text
