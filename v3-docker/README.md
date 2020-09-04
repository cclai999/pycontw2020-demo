#Prerequisites
## 建立執行環境
這個專案的開發環境使用 MacOS Docker version 19.03.12, build 48a66213fe

## 程式執行
1. 先進入 docker-base 目錄, build aibase:0.1.01beta image, 這個 image 會安裝好 python 3.8, Flask, torch &
torchvision
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

3. 回到 v3-docker 目錄, 利用 docker-compose 建立 aimodel image
```shell script
v3-docker$ docker-compose build
```

4. 用 docker image 指令應該可以看到類似以下的訊息
```shell script
v3-docker$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
aimodel             pycontw2020         35fc11000b60        11 seconds ago      1.91GB
aibase              0.1.01beta          d33c3b6070da        5 minutes ago       1.73GB
python              3.8                 a7cda474cef4        2 days ago          882MB
```

5. docker-compose up 啟動 aimodel docker
```shell script
v3-docker$ docker-compose up -d
```
```shell script
v3-docker$ docker ps -a
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                     NAMES
3481eb51d96a        aimodel:pycontw2020   "/bin/sh -c 'gunicor…"   51 seconds ago      Up 49 seconds       0.0.0.0:15000->5000/tcp   v3-docker_aimodel_1
```

6. 利用 curl call ai api
```shell script
$ curl -X POST -H "Content-Type: application/json" -d '{"img_url" : "dog.jpg"}' "http://localhost:15000/api/imgnet"
{"class_name":"Labrador retriever","img_url":"dog.jpg","percentage":48.25559997558594,"status":"success","status_code":200}
```

7. 利用 docker-compose down 停止 docker container
```shell script
v3-docker$ docker-compse down
```