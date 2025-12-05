text = "My Name is Vinit"

result_dict = {}

for char in text:
    if char != ' ':  # Skip whitespace characters
        if char in result_dict:
            result_dict[char] +=1
        else:
            result_dict[char] = 1

print(result_dict)  