input_str = str(input("Enter a string: "))

def check_string_only(input_str):
    if input_str.isalpha():
        return True
    else:
        return False


print(f"Entered string contains only alphabets" if check_string_only(input_str) else f"Entered string contains non-alphabet characters")