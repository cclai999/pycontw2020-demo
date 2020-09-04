import torch
from torchvision import models
from torchvision import transforms
from PIL import Image


class MyResnet():
    def __init__(self, model_state_path: str, classes_names_path: str):
        # load the model
        self._model = models.resnet101(pretrained=False)
        state_dict = torch.load(model_state_path)
        self._model.load_state_dict(state_dict)
        # put the network in eval mode
        self._model.eval()
        # create an image transform
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )])
        # load names of all classes
        with open(classes_names_path) as f:
            self.classes = [line.strip() for line in f.readlines()]

    def predict(self, img: Image):
        img_t = self.transform(img)
        batch_t = torch.unsqueeze(img_t, 0)

        # carry out model inference
        out = self._model(batch_t)

        _, index = torch.max(out, 1)
        percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
        return self.classes[index[0]], percentage[index[0]].item()

# # Forth, print the top 5 classes predicted by the model
# _, indices = torch.sort(out, descending=True)
# percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
# print([(classes[idx], percentage[idx].item()) for idx in indices[0][:5]])
