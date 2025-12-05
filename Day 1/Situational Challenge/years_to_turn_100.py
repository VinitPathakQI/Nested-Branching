name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

def calculate_years_to_100(age):
    years_left = 100 - age
    return years_left



result = calculate_years_to_100(age)
print(f"{name}, you have {result} years left to turn 100 years old.")