words = [
    "able lost darkness learn",
    "road older goes",
    "basic",
    "must seed laid itself hot must",
    "compound decide",
    "trap active paragraph hair review stay written",
    "facing smile vowel chose other",
    "occur shop box metal equal mouse some city"
]
# large = 0
# for string in words:
#     count = len(string.split())
#     if count > large:
#         large = count
#         long_str = string

# print(count)
# print(long_str)

longest_str = (max(len(string.split()) for string in words))

print(longest_str)