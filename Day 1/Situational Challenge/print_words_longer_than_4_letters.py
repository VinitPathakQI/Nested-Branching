import re

def find_long_words(text):
    words = re.findall(r"\b\w+'\w+|\w+\b", text.lower())
    long_words = [word for word in words if len(word) >= 4]
    return long_words



text = input("Enter a sentence: ")
result = find_long_words(text)
print("Words longer than 4 letters are: ", result)
