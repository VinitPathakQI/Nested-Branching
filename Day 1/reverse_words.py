def reverse_words(string):
    my_word = string.lower().split()
    reversed_words = []

    for word in range(len(my_word)-1, -1, -1):
        reversed_words.append(my_word[word])
    
    return ' '.join(reversed_words)


my_string = str(input("Enter the string: "))
print("Original String:", my_string)
print("Reversed String:", reverse_words(my_string))