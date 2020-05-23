import io, os
from os import path
# from numpy import random
from google.cloud import vision
from pillow_util import crop_image, draw_borders, Image
from sheet import insert_in_sheet
# import pandas as pd
import shutil

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"visionkey.json"
client = vision.ImageAnnotatorClient()

black_list = ["cuisine", "ingredient", "dish", "food", "foods", "family", "rice noodles", "soup", "fruit", "dessert",
              "snack cake", "baked goods", "none", "produce", "staple food", "recipe", "comfort food", "green",
              "fried food", "breakfast", "junk food", "meat", "natural foods", "yellow", "black", "product",
              "vegetable", "plant", "leaf", "nose", "footwear", "hair", "neck", "powder"
              
              "flower", "paper", "plastic", "utensils", "bottle", "glass", "preservatives", "sodium", 
              "sulfate", "ammonium", "solvents", "games", "bleach", "oxydent","silicons", "parabens", "group"
              "plastic bags", "napkins", "plates", "paper", "bleach", "natural", "herbal", "kettle", "spoon", 
              "fork", "knife", "dog food", "cat food", "books", "bunny", "gluten", "phthalates", "insoluble", 
              "formulas", "talc", "mineral", "sanitizer", "blocks", "donut", "ribbons", "item", "stack", "table",
              "chopsticks", "candles", "needles", "board", "natural", "medicine", "fats", "animal oil", "musks", 
              "paper plates", "plastic utensils", "sparkling", "scissors", "kits", "kettle", "books", "jar", 
              "fragrances", "vanilla", "alcohol", "wine", "beer", "vodka", "dark", "bug", "calories", "object"]

file_name = "vegg2.jpg"
image_path = os.path.join("./images/", file_name)

with io.open(image_path, "rb") as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.object_localization(image=image)
localized_object_annotations = response.localized_object_annotations

tag_list = []
def filter_tag_list(label_list):
    for label in label_list:
        new_label = label.description.split(" ")[-1].lower()
        # new_label = label.description.lower()
        if label.description in black_list or new_label in black_list:
            continue
        else:
            if new_label in tag_list:
                continue
            else:
                tag_list.append(new_label)
                break

index = 0
dirpath = ""
file_list = []
for obj in localized_object_annotations:
    pillow_image = Image.open(image_path)

    img = crop_image(pillow_image, obj.bounding_poly, pillow_image.size)
    dirname = "images/" + (pillow_image.filename.split("/")[-1]).split(".")[0]
    dirpath = dirname

    if not path.exists(dirname):
        os.mkdir(dirname)

    filename = dirname + "/" + str(index) + ".jpg"
    img.save(filename)
    file_list.append(filename)
    index += 1


for file in file_list:
    with io.open(file, "rb") as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    filter_tag_list(labels)

insert_in_sheet(tag_list)
shutil.rmtree(dirpath)

#
# # Visualization purpose
# df = pd.DataFrame(columns=["name", "score"])
# for obj in localized_object_annotations:
#     df = df.append(
#         dict(
#             name=obj.name,
#             score=obj.score
#         ),
#         ignore_index=True
#     )
#
# pillow_image = Image.open(image_path)
# for obj in localized_object_annotations:
#     r, g, b = random.randint(0, 155), random.randint(0, 155), random.randint(0, 155)
#
#     draw_borders(pillow_image, obj.bounding_poly, (r, g, b), pillow_image.size, obj.name, obj.score)
#
# pillow_image.show()
