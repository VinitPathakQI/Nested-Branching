print("Number divisible by 3 but not by 5: ")
for i in range(1,51):
    if i % 3 == 0 and i % 5 != 0:
        print(i)