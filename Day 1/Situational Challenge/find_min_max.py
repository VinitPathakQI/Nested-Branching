numbers = list(map(int, input("Enter numbers: ").split()))

def find_min_max(*values):
    if len(values) == 0:
        return None
    min_value = values[0]
    max_value = values[0]

    for num in values[1:]:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    return min_value, max_value


min_value, max_value = find_min_max(*numbers)
print(f"Min value: {min_value}, Max value: {max_value}")
