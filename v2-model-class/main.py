import json
from PIL import Image
from model import MyResnet

# img = Image.open("../test-data/bobby.jpg")
img = Image.open("../test-data/cat.jpg")
# img = Image.open("../test-data/dog.jpg")
# img = Image.open("../test-data/dog_briard.jpg")
# img = Image.open("../test-data/man_hole.jpg")
# img = Image.open("../test-data/velvet.jpg")
# img = Image.open("../test-data/violin.jpg")

imgnet = MyResnet("../model-state/resnet101-5d3b4d8f.pth", "../model-state/imagenet_classes.txt")

class_name, percentage = imgnet.predict(img)
result = {
    "class": class_name,
    "percentage": percentage
}
print(json.dumps(result))
