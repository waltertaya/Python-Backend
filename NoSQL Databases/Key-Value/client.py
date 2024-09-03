import requests
import json

BASE_URL = 'http://localhost:8000'

def add_user(username, user_data):
    url = f'{BASE_URL}/user'
    payload = {
        'username': username,
        'data': user_data
    }
    response = requests.post(url, json=payload)
    print(f'POST /user response: {response.status_code}')
    print(response.json())

def get_user(username):
    url = f'{BASE_URL}/user/{username}'
    response = requests.get(url)
    print(f'GET /user/{username} response: {response.status_code}')
    print(response.json())

if __name__ == '__main__':
    user_data = {
        'email': 'brettcooper@example.com',
        'age': '30',
        'location': 'New York'
    }
    add_user('brettcooper', user_data)

    get_user('brettcooper')
