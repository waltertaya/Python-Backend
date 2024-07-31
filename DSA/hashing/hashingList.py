def hashing(arr):
    '''
    return hash table
    For conflict resolution => (Open addressing) Double hashing
    '''
    hashtable = {}
    for i in arr:
        ascii_total = 0
        for char in i:
            ascii_total += ord(char.lower())
        if ascii_total in hashtable.keys():
            ascii_total *= 2
        hashtable[ascii_total] = i
    return hashtable
