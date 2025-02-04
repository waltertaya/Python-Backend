import base64

from rembg import remove
from PIL import Image
import io

from flask import request, jsonify


def register_routes(app):
    @app.route('/removebg', methods=['POST'])
    def removebg():
        data = request.json
        img_data = base64.b64decode(data['image'])

        with open('image.png', 'wb') as f:
            f.write(img_data)
        
        input_path = 'image.png'
        with open(input_path, "rb") as f:
            input_data = f.read()

        # input_data = Image.open(io.BytesIO(img_data))

        output_data = remove(input_data)

        return jsonify({'image': base64.b64encode(output_data).decode('utf-8')})
