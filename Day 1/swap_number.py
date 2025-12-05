'''
Swap Two Variables Without Using a Temp Variable
'''

def swap_number(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

val1 = int(input("Enter value 1: "))
val2 = int(input("Enter value 2: "))
a,b = swap_number(val1,val2)

print(f"a: {a}, b: {b}")