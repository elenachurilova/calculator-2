"""CLI application for a prefix-notation calculator."""

# from arithmetic import (add, subtract, multiply, divide, square, cube,
#                         power, mod, )


while True:

    user_input = input("Please enter your equasion > ")

    tokens = user_input.split(" ")


    if tokens[0] == "q":
        print("You requested to exit...")


    #Handling cases when user only need to enter 2 pieces of equasion
    if len(tokens) < 3:

        func = tokens[0]
        num1 = tokens[1]

    #For cases when there should be 3 pieces of equasion
    if len(tokens) == 3:

        func = tokens[0]
        num1 = tokens[1]
        num2 = tokens[2]

    #All operator functions - complete logic:
    if func == "+":
        print((float(num1)) + (float(num2)))

    if func == "-":
        print((float(num1)) - (float(num2)))

    if func == "*":
        print((float(num1)) * (float(num2)))

    if func == "/":
        print((float(num1)) / (float(num2)))      

    if func == "square":
        print((float(num1)) ** 2)

    if func == "cube":
        print((float(num1)) ** 3)

    if func == "pow":
        print(pow(float(num1),float(num2)))

    if func == "mod":
        print((float(num1)) % (float(num2))) 


# Replace this with your code
