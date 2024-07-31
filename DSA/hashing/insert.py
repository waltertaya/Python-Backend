from hashingFunction import hashAlgorithm
import json

def insert_element():
    with open('data.json', 'r') as f:
            json_data = f.read()

    hashtable = json.loads(json_data)

    x = input('Enter the element to insert into the database: ')
    key = hashAlgorithm(x)
    hashtable[key] = x

    json_data = json.dumps(hashtable)

    with open('data.json', 'w') as f:
        f.write(json_data)
    
    return hashtable
