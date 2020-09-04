#Prerequisites
## 建立執行環境
這個專案的開發環境使用 Pyhton 3.8.5
若你是採用 conda 管理 virtual environment, 可以利用以下的指令建立執行環境
```shell script
$ conda create --name aimodel python=3.8.5
$ conda activate aimodel  #啟用虛擬環境
$ pip install -r requirements.txt
```
## 程式執行
```shell script
$ python main.py
```
預期結果
```shell script
{"class": "tabby, tabby cat", "percentage": 71.4230728149414}
```


