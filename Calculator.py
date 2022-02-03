# Calculator
import math
from time import sleep

# Return & parameter
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# no return 
def power (x,y):
    print(x ** y) 

def square_root (x):
    print(math.sqrt(x))

def logarithm (x,y):
    print(math.log(num1,num2))

def sine(x):
    print(math.sin(x))

# no return no parameter
def breaking():
    import sys
    print(" Exit")
    sleep(10)
    sys.exit()

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponentiation")
print("6.Logarithm")
print("7.Square Root")
print("8.Sine")
print("9.Exit")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

    # check if choice is one of the six options
    if choice in ('1', '2', '3', '4','5','6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            print(num1, "^", num2, "=")
            power(num1,num2)

        elif choice == '6':
            print("log(",num1, ",", num2,  ") = ")
            logarithm(num1,num2)      
        
    elif choice in ('7','8'):

        num1 = float(input("Enter number: "))

        if choice == '7':
            print(num1,"^ 1/2 =")
            square_root(num1)

        elif choice == '8':
            print(num1, "=")
            sine(num1)

    elif choice =='9':
            breaking()
    
    else:
        print("Invalid Input")