# pycontw2020-demo
這個專案包含了我在 PyCon Taiwan 2020 分享 - [我們如何在醫院打造即時醫療影像AI平台](https://tw.pycon.org/2020/zh-hant/conference/talk/1163619671685988728/) -
的 demo 程式碼。

## Prerequisites
請先下載 PyTorch RestNet101 pretrain model, [下載連結](https://download.pytorch.org/models/resnet101-5d3b4d8f.pth)  
然後 copy model 到以下目錄:
1. [model-state](./model-state)
2. [v2-model-class/model](./v2-model-class/model)
3. [v3-docker/model](./v3-docker/model)
4. [v4-docker-w-minio](./v4-docker-w-minio/model-state)

## How to run demo code?
每個目錄都有自己的 README.md 說明如何執行
