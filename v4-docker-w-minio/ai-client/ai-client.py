import sys
from minio import Minio
from minio.error import ResponseError
import requests

minioClient = Minio('127.0.0.1:9000',
                    access_key='minio',
                    secret_key='minio123',
                    secure=False)
try:
    s1 = minioClient.fput_object('mybucket', 'violin.jpg', 'violin.jpg')
except ResponseError as err:
    print(f"File upload error: {err}")
    sys.exit()

r = requests.post('http://127.0.0.1:15000/api/imgnet', json={"img_url": "violin.jpg"})
if r.status_code == 200:
    print(r.text)
else:
    print(r.text)

