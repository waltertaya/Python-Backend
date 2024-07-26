import requests

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://127.0.0.1:3000/api'

response = requests.get(endpoint, json={"query": "Hello World"})

# print(response.text)
print(response.json())
print(response.status_code)
