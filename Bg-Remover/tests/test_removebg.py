import requests
import base64

def test_removebg_api_route():

    input_path = 'tests/test_image.jpg'
    output_path = 'tests/test_output.jpg'

    with open(input_path, 'rb') as f:
        img_data = f.read()

    data = {'image': base64.b64encode(img_data).decode('utf-8')}

    # print(data)
    response = requests.post('http://localhost:5000/removebg', json=data)

    # print(response.json())

    with open(output_path, 'wb') as f:
        f.write(base64.b64decode(response.json()['image']))

    assert response.status_code == 200
    assert response.json()['image'] is not None
    # assert response.json()['image'] == data['image']


if __name__ == '__main__':
    test_removebg_api_route()