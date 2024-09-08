from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    result = {
        'message': 'Reached the flask app'
    }
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=False, port=8000)
