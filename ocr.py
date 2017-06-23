import tesserocr
from PIL import Image
from io import BytesIO

print(tesserocr.get_languages())


def image_to_text(image):
    image_data = image[0][1].read()
    image_object = Image.open(BytesIO(image_data))
    #image_image = tesserocr.PyTessBaseAPI.SetImageBytes(image_data)
    text = tesserocr.image_to_text(image_object, 'rus')
    return text
