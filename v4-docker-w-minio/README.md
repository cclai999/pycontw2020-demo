#Prerequisites
## 建立執行環境
這個專案的開發環境使用 MacOS Docker version 19.03.12, build 48a66213fe

## 程式執行
1. 先進入 docker-base 目錄, build aibase:0.1.01beta image, 這個 image 會安裝好 python 3.8, Flask, torch &
torchvision
PS: 有已先執行過 v3-docker demo code, 則不必再重新 build
```shell script
docker-base$ docker build -t aibase:0.1.01beta .
```

2. 建立好 image, 可以用 docker image 指令應該可以看到類似以下的訊息
```shell script
docker-base$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
aibase              0.1.01beta          d33c3b6070da        59 seconds ago      1.73GB
python              3.8                 a7cda474cef4        2 days ago          882MB
```

3. 回到 v4-docker-w-minio 目錄, 利用 docker-compose 建立 aimodel2 image
```shell script
v4-docker-w-minio$ docker-compose build
```

4. 用 docker image 指令應該可以看到類似以下的訊息
```shell script
v4-docker-w-minio$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
aimodel2            pycontw2020         efbf1f5b9d8b        45 seconds ago      1.74GB
aibase              0.1.01beta          d33c3b6070da        17 minutes ago      1.73GB
python              3.8                 a7cda474cef4        2 days ago          882MB
```

5. docker-compose up 啟動 aimodel2 & minio docker
```shell script
v4-docker-w-minio$ docker-compose up -d
```
```shell script
v4-docker-w-minio$ docker ps -a
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                     NAMES
38b70bffeec8        minio/minio            "/usr/bin/docker-ent…"   19 seconds ago      Up 18 seconds       0.0.0.0:9000->9000/tcp    minio
96372fa97c41        aimodel2:pycontw2020   "/bin/sh -c 'gunicor…"   19 seconds ago      Up 18 seconds       0.0.0.0:15000->5000/tcp   v4-docker-w-minio_aimodel_1
```

6. 安裝相關 pyhton package
```shell script
v4-docker-w-minio$ pip listall -r requirements.txt 
```

7. 進行 ai-client 目錄, 執行 ai-client.py
```shell script
v4-docker-w-minio$ python ai-client.py 
{"class_name":"violin, fiddle","img_url":"violin.jpg","model_name":"ResNet101","model_version":1.0,"percentage":99.7668685913086,"status":"success","status_code":200}
```