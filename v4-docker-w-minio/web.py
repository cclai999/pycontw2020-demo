from pathlib import Path
import io
from flask import Flask, request, jsonify
import yaml
from PIL import Image
from minio import Minio
from model import MyResnet

app = Flask(__name__)

model_config = yaml.safe_load(open('./model-state/config.yaml', 'r'))
model_state_file = Path('./model-state') / model_config['MODEL_STATE_FILE']
model_classes_file = Path('./model-state') / model_config['MODEL_CLASSES_FILE']
imgnet = MyResnet(model_state_file, model_classes_file)

minioClient = Minio('minio:9000',
                    access_key='minio',
                    secret_key='minio123',
                    secure=False)


def get_minio_img(img_url):
    resp = minioClient.get_object("mybucket", img_url)
    return Image.open(io.BytesIO(resp.data))


@app.route('/api/imgnet', methods=['POST'])
def inference():
    req_data = request.get_json()
    if req_data.get('img_url', None):
        img = get_minio_img(req_data["img_url"])
        class_name, percentage = imgnet.predict(img)
        result = {
            "status": "success",
            "status_code": 200,
            "img_url": req_data['img_url'],
            "class_name": class_name,
            "percentage": percentage,
            "model_name": model_config['AIMODEL_NAME'],
            "model_version": model_config['AIMODEL_VERSION'],
        }
        return jsonify(result), 200
    else:
        return f'"img_url" data not found in request body!', 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
