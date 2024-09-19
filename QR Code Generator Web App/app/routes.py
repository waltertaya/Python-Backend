from flask import request, send_file, render_template
import qrcode
from io import BytesIO

def register_routes(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/generate_qr', methods=['POST'])
    def generate_qr():
        data = request.form.get('data')
        if not data:
            return "No data provided", 400

        img = qrcode.make(data)
        
        buf = BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        
        return send_file(buf, mimetype='image/png', as_attachment=True, download_name='qrcode.png')
