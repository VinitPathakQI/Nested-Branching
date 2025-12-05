def get_ascii_value(s):
    for char in s:
        print(f"{char}: {ord(char)}")


str = input("Enter a string: ")
get_ascii_value(str)

