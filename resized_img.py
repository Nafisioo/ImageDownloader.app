from PIL import Image

async def resize_image(img, target_size=(224, 224)):
    return img.resize(target_size)