from PIL import Image
import io

def readImage(file) -> Image.Image:
    image = Image.open(io.BytesIO(file))
    return image.convert("RGB")