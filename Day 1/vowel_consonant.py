'''
Count Vowels and Consonants
Input: "Hello World" → Output: Vowels: 3, Consonants: 7
'''

def count_vowel_and_consonant(str):
    vowels = 'aeiou'
    count_vowel = 0
    count_consonant = 0

    for char in str.lower():
        if char in vowels:
            count_vowel +=1
        else:
            count_consonant +=1
    return count_vowel, count_consonant



input_str = str(input("Enter the string: "))
vowel_count, consonant_count = count_vowel_and_consonant(input_str)
print(f"Vowel: {vowel_count}, Consonant: {consonant_count}")