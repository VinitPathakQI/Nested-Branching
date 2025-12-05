import re

text = "This isn't my day! and, this day is very bad..."

result = {}
words = re.findall(r"\b\w+'\w+|\w+\b", text.lower())
# words = text.lower().split()    
for word in words:
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)


r'''
\b: Word boundary: It matches the position between a word character(like a letter, digit, or underscore) and a non-word character (like a space or punctuation).
\w: Matches any word character (equivalent to [a-zA-Z0-9_])
\w+: One or more word characters: This matches sequences of word characters, effectively capturing whole words.
\w+'\w+ = handles contractions like isn't, don't, etc.

so \b\w+'\w+|\w+\b: Words with apostrophes (like Isn't) or regular words (like day)
'''