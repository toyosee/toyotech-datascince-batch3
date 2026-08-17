# Data Types
# Definition: Representation of data
# string, number (int, float, complex, boolean, none)

# greeting = "Hello World"
# age = 6
# salary = 567.89
# isCooking = True
# type_checker = type(isCooking)
# print(type_checker)

# Number checker
# my_var = "6r"
# if my_var.isdigit():
#     new_var = float(my_var)
#     print(new_var)
# else:
#     print("Please eneter a valid number")

# Data structures -

# # list
# books = ["Journey to the center of earth", 45, 56.6, None, True]
# coordinates = list((22.3, 56.6))
# coordinates[0] = 13.3
# # print(coordinates)

# my_dict = {
#     "name": "Tolu",
#     "Address": "Murtala square",
#     "salary": 5_000_000_000
# }

# # salary = my_dict["salary"]
# # print(salary)

# collections = ["Journey to the center of earth", 45, 56.6, None, True]
# print(collections)

# number = 5.7

# if isinstance(number, int):
#     print("You win")
# elif isinstance(number, float):
#     print("You Loose")
# else:
#     print("Please enter a valid number")

# Operators

# Floor divisio //
# var1 = 5
# var2 = 7

# compare = var1 != var2
# # print(compare)

# shoes = 8
# shoes /= 2

# addy = "barnawa is a place"
# print(addy.split(" "))

# my_mail= " int@yahoo.com  "
# print(my_mail[0:4])
# splitter = my_mail.split("@")
# username = splitter[0]
# domain_name = splitter[1]
# print("Your username is ",username[0])
# print("Your domain is ",domain_name)

# String interpolation
# f_name = "Isaac"
# l_name = "Newton"

# print(f"My name is {f_name} and my last name is {l_name}")

# # Formatting Numbers
# price = 19.9999
# print(type(price))
# converted_price = f"price:.4f"
# print(type(converted_price)) # Price: $20.00

# my_data = "Python"
# print(my_data[::-1])

favorites = [2, 4, "Mustapha", ["yam", "egg"], True, [False, None]]
protein = favorites[3][1]
print(protein)

# range(start, stop, step)
numbers = list(range(1, 20, 2))
square_numbers = []
for number in numbers:
    # do something
    number **= 2
    square_numbers.append(number)
# square_numbers = [number ** 2 for number in numbers]
print(square_numbers)