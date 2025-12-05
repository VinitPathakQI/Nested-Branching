
def greet_user(name, age):
    return f"Hello {name}! You are {age} years old."



name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
greeting = greet_user(name, age)

print(greeting)