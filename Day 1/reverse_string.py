'''
Reverse a String (without slicing)
# Input: "python" → Output: "nohtyp"
'''


def reverse_str(str):
    reversed_str = ''
    for char in str.lower():
        reversed_str = char + reversed_str
    return reversed_str

string = str(input("Enter the string: "))
print(reverse_str(string))
