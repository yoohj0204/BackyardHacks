import io
from PIL import Image, ImageDraw, Image, ImageFont
# import cv2

def crop_image(pillow_image, bounding, image_size):
    width, height = image_size

    left = bounding.normalized_vertices[0].x * width
    top = bounding.normalized_vertices[0].y * height
    right = bounding.normalized_vertices[2].x * width
    bottom = bounding.normalized_vertices[2].y * height

    img = pillow_image.crop((left, top, right, bottom))

    return img

def draw_borders(pillow_image, bounding, color, image_size, caption="", confidence_score = 0):
    width, height = image_size
    draw = ImageDraw.Draw(pillow_image)
    draw.polygon([
        bounding.normalized_vertices[0].x * width,
        bounding.normalized_vertices[0].y * height,
        bounding.normalized_vertices[1].x * width,
        bounding.normalized_vertices[1].y * height,
        bounding.normalized_vertices[2].x * width,
        bounding.normalized_vertices[2].y * height,
        bounding.normalized_vertices[3].x * width,
        bounding.normalized_vertices[3].y * height
    ], fill=None, outline=color)

    font_size = width * height
    font = ImageFont.truetype(r"C:/Users/y7ahf/AppData/Local/Microsoft/Windows/Fonts/open-sans/OpenSans-Regular.ttf", 16)
    draw.text((bounding.normalized_vertices[0].x * width,
                bounding.normalized_vertices[0].y * height), font=font, text=caption, fill=color)

    #insert confidence score
    draw.text((bounding.normalized_vertices[0].x * width, bounding.normalized_vertices[0].y * height + 20),
                font=font, text="Confidence Score: {0:.2f}%".format(confidence_score), fill=color)

    return pillow_image
