"""
    programmer error (error) SyntaxError
    program error (bug)
    program exception (exception)
"""

# bug
# number1 = input("please enter a number: ")
# number2 = input("please enter another number:")

# print(number1, "+", number2, "=", number1 + number2)


# exception

# number1 = input("number1: ")
# number2 = input("number2: ")

# number1 = int(number1)
# number2 = int(number2)

# ValueError: invalid literal for int() with base 10: 'dsfa' or ZeroDivisionError: division by zero
# print(number1, "/", number2, "=", number1 / number2)

# number3 = input("number3: ")
# number4 = input("number4: ")

# try:
#     number3 = int(number3)
#     number4 = int(number4)
#     print(number3, "/", number4, "=", number3 / number4)
# except ValueError:
#     print("Please enter a number")
# except ZeroDivisionError:
#     print("Cannot divide by 0")


# Except as

# try:
#     number3 = int(number3)
#     number4 = int(number4)
#     print(number3, "/", number4, "=", number3 / number4)
# except ValueError as e:
#     print("e", e)


# finally

try:
    file = open("filename", "r")
except IOError as e:
    print("e", e)
finally:
    file.close()


# raise

try:
    number3 = int(input("number3: "))
    number4 = int(input("number4: "))
    if number4 == 23:
        raise ZeroDivisionError("23 is not allowed as a denominator")
    print(number3, "/", number4, "=", number3 / number4)
except (ValueError, ZeroDivisionError) as e:
    print("e", e)
