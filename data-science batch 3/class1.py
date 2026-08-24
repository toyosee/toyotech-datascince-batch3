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

# favorites = [2, 4, "Mustapha", ["yam", "egg"], True, [False, None]]
# protein = favorites[3][1]
# print(protein)

# # range(start, stop, step)
# numbers = list(range(1, 20, 2))
# square_numbers = []
# for number in numbers:
#     # do something
#     number **= 2
#     square_numbers.append(number)
# # square_numbers = [number ** 2 for number in numbers]
# print(square_numbers)

# age = 19
# isLicensed = True

# if age >= 18 and isLicensed == True:
# #     print("Allowed to drive")
# # else:
# #     print("Sorry not allowed to drive")

# allowed_roles = ["admin", "staff", "user"]
# user_role = "staff"

# if user_role in allowed_roles:
#     print("Login successful")
#     if user_role == "admin":
#         print("Welcome to Admin dashboard")
#     elif user_role == "staff":
#         print("Welcome to Staff Dashboard")
#     elif user_role == "user":
#         print("Welcome to User Dashboard")
#     else:
#         print("Go back to Login")
# else:
#     print("Unauthorized")

# LOOPS - for / while
# FOR
# BU$BE$$Y
# designer = "Burberry"
# # for char in designer:
#     if char == "r":
#         char = "$"
#     char = char.upper()
#     print(char)

# may = "r"
# print("R" == may)

# cole = list(range(1,7))
# for num in cole:
#     if num == 4:
#         continue
#     print(num)
# starter = 1

# while starter <= len(cole):
#     print(starter)
#     starter += 1

# Functions
# Predefined - user defined - lambda

# print(), range(), len()

# user defined
# def myGuy(name, hour):
#     print(f"Good {name.upper()} {hour.title()}")
    
# name = "Elijah"
# time = "Afternoon"
# myGuy(time, name)

# def incrementAge(*args):
#     return args

# # age = 73
# # new_Age = incrementAge(3,4,5,6,7,8,9,5)
# # print(new_Age)

# def squareIt(num):
#     num **= 2
#     return num


# print((lambda base,height: 0.5 * base * height)(4,3))

# def performOperations(operator, val1, val2):
#     result = None
#     if operator == "+":
#         result = val1 + val2
#     elif operator == "-":
#         result = val1 - val2
#     elif operator == "tri":
#         result = 0.5 * val1 * val2
#     else:
#         result = "Something went wrong"
#     return result


# print(performOperations("tri",5,5))

# # Enum - enumerate()
# items = ["",6,True]
# definer = enumerate(items)
# for something in definer:
#     print(something)
    
# height = [4.5, 6.7, 3.2]
# name = ["Simon", "Joseph", "Zach"]
# combo = zip(height,name)
# print(list(combo))

# # *args, **kwargs

# def addiIt(*args):
#     return type(args)

# # print(addiIt(3,4,5,6,7,8,9))

# def biggerArgs(**kwargs):
#     all_items = kwargs.keys()
#     return all_items

# print(biggerArgs(name="Theophilus", address ="", age=67))

# Aplication of args and kwargs
# Creating flexible configuration functions
def configure(**kwargs):
    config = {
    'debug': False,
    'timeout': 30,
    'max_retries': 3
    }
    config.update(kwargs)
    return config

settings = configure(debug=True, timeout=60, custom_option="value", url="https://something.com ")
print(settings.get("url"))
