'''
Check Whether a Number is Even or Odd
'''


def is_even_or_odd(num):
    if num < 0:
        return None
    return num % 2 == 0
        


input_num = int(input("Enter the number: "))
print(f"{input_num} is Even" if is_even_or_odd(input_num) else f"{input_num} is Odd" )