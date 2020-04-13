"""
Ching Han Huang
113510994
10/03/19

Assignment 4 : Practice with functions
"""

a = 1
b = 1

# add function : assign the summation value of number1 and number 2 to number2
def addNum(num1, num2):
    num2 = num1 + num2
    return num2

# subtract function : assign the subtraction of number1 and number2 to number1
def subtractNum(num1, num2):
    num1 = num2 - num1
    return num1

# mutiplu function : assign the multiplication of number1 and number2 to number2
def multiplyNum(num1, num2):
    num2 = num1 * num2
    return num2

# Before enter the while loop, assign a value to response variable. 
response = input('What would you like to do (print, quit, add, subtract, multiply)')

# Use while loop to check the user's response. If response is not 'quit', then it will enter the loop. 
# And according to the user's response, the code will execute different functions.
while response != 'quit':

    if response == 'print':
        print("The value of a is ", a, " and the value of b is ", b)

    elif response == 'add':
        b = addNum(a, b)

    elif response == 'subtract':
        a = subtractNum(a, b)

    elif response == 'multiply':
        b = multiplyNum(a, b)

    response = input('What would you like to do (print, quit, add, subtract, multiply)')

# If the user's reaponse is 'quit', the program will stop.
if response == 'quit':
    print("Thanks for using my program.")  