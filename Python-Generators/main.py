some_words = ['Strong', 'wise', 'handsome', 'brave', 'kind',
              'humble', 'funny', 'generous', 'loyal', 'courageous',
              'intelligent', 'charming', 'confident', 'determined',
              'boy', 'creative']

# def contain_e(words):
#     result = []
#     for word in words:
#         if 'e' in word:
#             result.append(word)
#     return result

def contain_e(words):
    for word in words:
        if 'e' in word:
            yield word


if __name__ == '__main__':
    print(contain_e(some_words))
    print(list(contain_e(some_words)))

    obj = contain_e(some_words)

    print(next(obj))
    print(next(obj))
    print(next(obj))
