from flask import Flask, request, jsonify
from PIL import Image
from model import MyResnet

app = Flask(__name__)
imgnet = MyResnet("model/resnet101-5d3b4d8f.pth", "model/imagenet_classes.txt")


# curl -X POST -H "Content-Type: application/json" -d '{"img_url" : "dog.jpg"}' "http://localhost:5000/api/imgnet"
@app.route('/api/imgnet', methods=['POST'])
def inference():
    req_data = request.get_json()
    if req_data.get('img_url', None):
        img = Image.open("./test-data/" + req_data["img_url"])
        class_name, percentage = imgnet.predict(img)
        result = {
            "status": "success",
            "status_code": 200,
            "img_url": req_data['img_url'],
            "class_name": class_name,
            "percentage": percentage,
        }
        return jsonify(result), 200
    else:
        return f'"img_url" data not found in request body!', 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
