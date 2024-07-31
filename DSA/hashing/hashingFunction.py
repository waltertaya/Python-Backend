def hashAlgorithm(str):
    '''
    Use the hash function to provide the key
    Conflict Resolution => (open addressing) : Double hashing
    '''
    ascii_total = 0
    for char in str:
        ascii_total += ord(char.lower())
    return ascii_total
