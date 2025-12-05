'''
Calculate the Sum of Digits of a Number
'''

def sum_of_numbers(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum


number = int(input("Enter the number: "))
print(f"Sum of {number} is : {sum_of_numbers(number)}")