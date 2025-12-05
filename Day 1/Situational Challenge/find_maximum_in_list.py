# value_1 = int(input("Enter first value: "))
# value_2 = int(input("Enter second value: "))
# value_3 = int(input("Enter third value: "))

numbers = list(map(int, input("Enter numbers: ").split()))

def find_maximum_of_three_number(*values):
    if len(values) == 0:
        return None
    max_value = values[0]

    for num in values[1:]:
        if num > max_value:
            max_value = num
    return max_value


max_value = find_maximum_of_three_number(*numbers)

print(f"The max value is: {max_value}")
    
