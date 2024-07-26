import requests

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://127.0.0.1:3000/api/'

# response = requests.get(endpoint, json={"query": "Hello World"})
data = {
    "title": "White pepper",
    "description": "Grinded white pepper, canned in tin of 300 grams",
    "price": 207,
}

response = requests.post(endpoint, data=data)

# print(response.text)
print(response.json())
print(response.status_code)
