import base64

from rembg import remove
from PIL import Image

from flask import request, jsonify


def register_routes(app):
    @app.route('/removebg', methods=['POST'])
    def removebg():
        data = request.json
        img_data = base64.b64decode(data['image'])

        with open('image.png', 'wb') as f:
            f.write(img_data)
        
        input_path = 'image.png'
        output_path = 'output.png'
        remove(input_path, output_path)

        with open(output_path, 'rb') as f:
            output_img = f.read()
        
        return jsonify({'image': base64.b64encode(output_img).decode('utf-8')})
