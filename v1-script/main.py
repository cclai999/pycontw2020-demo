import torch
from torchvision import models
from torchvision import transforms
from PIL import Image

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )])

# img = Image.open("../test-data/bobby.jpg")
img = Image.open("../test-data/cat.jpg")
# img = Image.open("../test-data/dog.jpg")
# img = Image.open("../test-data/dog_briard.jpg")
# img = Image.open("../test-data/man_hole.jpg")
# img = Image.open("../test-data/velvet.jpg")
# img = Image.open("../test-data/violin.jpg")

img_t = transform(img)
batch_t = torch.unsqueeze(img_t, 0)
with open('../model-state/imagenet_classes.txt') as f:
    classes = [line.strip() for line in f.readlines()]

# First, load the model
resnet = models.resnet101(pretrained=False)
state_dict = torch.load("../model-state/resnet101-5d3b4d8f.pth")
resnet.load_state_dict(state_dict)

# Second, put the network in eval mode
resnet.eval()

# Third, carry out model inference
out = resnet(batch_t)

_, index = torch.max(out, 1)
percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
print(classes[index[0]], percentage[index[0]].item())

# Forth, print the top 5 classes predicted by the model
# _, indices = torch.sort(out, descending=True)
# percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
# print([(classes[idx], percentage[idx].item()) for idx in indices[0][:5]])
