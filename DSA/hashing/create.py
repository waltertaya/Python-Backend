from hashingList import hashing

import json

if __name__ == '__main__':
    arr = ['Mia', 'Sam', 'Leo', 'Mia', 'Joe', 'Mitty', 'Taya', 'Jay', 'Brett', 'Cooper', 'John', 'Shay']
    hashtable = hashing(arr)
    json_data = json.dumps(hashtable)

    with open('data.json', 'w') as f:
        f.write(json_data)
