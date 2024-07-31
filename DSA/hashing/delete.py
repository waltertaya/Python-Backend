from hashingFunction import hashAlgorithm
import json

def delete_element():
    with open('data.json', 'r') as f:
            json_data = f.read()

    hashtable = json.loads(json_data)

    x = input('Enter the element to delete into the database: ')
    key = hashAlgorithm(x)
    try:
        del hashtable[str(key)]
    except Exception as e:
        #  raise KeyError('Element does not exist in the database')
        return KeyError('Element does not exist in the database')

    json_data = json.dumps(hashtable)

    with open('data.json', 'w') as f:
        f.write(json_data)
    
    return hashtable
