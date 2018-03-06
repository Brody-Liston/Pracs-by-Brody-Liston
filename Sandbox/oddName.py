"""Brody Liston"""
min_lenght = 1

user_name = str(input("Enter Name Please "))
while len(user_name) < min_lenght:
    print("Invalid Name Must not Be Blank")
    user_name = str(input("Enter Name Please "))

print((user_name)[::2])
