numbers = list(map(int, input("Enter numbers: ").split()))

def find_smallest_largest_second_largest(*values):
    smallest = values[0]
    largest = values[0]
    second_largest = float('-inf')

    for num in values:
        if num > largest:
            second_largest = largest
            largest = num
        if num > second_largest and num != largest:
            second_largest = num
        if num < smallest:
            smallest = num
    return smallest, largest, second_largest



smallest, largest, second_largest = find_smallest_largest_second_largest(*numbers)
print(f"Smallest: {smallest}\nLargest: {largest}\nSecond Largest: {second_largest}")
    



