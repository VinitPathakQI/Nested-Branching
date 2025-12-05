'''
Check if a String is a Palindrome
input : "madam", "racecar" → Palindrome
'''


def is_palindrome(value):
    left = 0
    right = len(value) - 1

    while left < right:
        if value[left] != value[right]:
            return False
        left += 1
        right -= 1
    return True


str_input = str(input("Enter the string: "))

if is_palindrome(str_input):
    print(f"{str_input} -> Palindrome")
else:
    print(f"{str_input} -> Not Palindrome")