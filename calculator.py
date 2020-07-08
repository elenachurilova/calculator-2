"""CLI application for a prefix-notation calculator."""

# from arithmetic import (add, subtract, multiply, divide, square, cube,
#                         power, mod, )


while True:

    user_input = input("Please enter your equasion > ")

    tokens = user_input.split(" ")

    func = tokens[0]
    num1 = tokens[1]
    num2 = tokens[2]

    if tokens[0] == "q":
        print("You requested to exit...")

    else:
        if func == "+":
            print((float(num1)) + (float(num2)))

        if func == "-":
            print((float(num1)) - (float(num2)))

        if func == "*":
            print((float(num1)) * (float(num2)))


# Replace this with your code
