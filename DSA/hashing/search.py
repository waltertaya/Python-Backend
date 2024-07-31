import json
from hashingFunction import hashAlgorithm

def search_name():
    with open('data.json', 'r') as f:
        json_data = f.read()

    hashtable = json.loads(json_data)

    x = input('Enter name to be searche in the database: ')

    hash_code = hashAlgorithm(x)

    if str(hash_code) in hashtable.keys():
        return True
    else:
        if str(hash_code * 2) in hashtable.keys():
            return True
        return False
