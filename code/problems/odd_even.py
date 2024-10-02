"""
Check if number is even or odd
"""
num = int(input("Enter a number: "))

my_dict = {0: "even"}

print("Result:", my_dict.get(num % 2, "odd"))
