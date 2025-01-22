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

# longest_str = (max(len(string.split()) for string in words))

string_list = (string.split() for string in words)
string_len = (len(string) for string in string_list)
longest_str = (max(string_len))

print(longest_str)