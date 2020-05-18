def main():
    print("1. Determine odd or even\n2. Determine bigger number\n3. Find sum of numbers\n4. Display even numbers")
    choice = input("\n\nEnter a choice: ")
    while choice.isnumeric() == False:
        choice = input("Enter a choice: ")
    return choice

def F1():
    number1 = input("Enter a number: ")
    while number1.isnumeric() == False:
        number1 = input("Enter a number: ")
    if int(number) % 2 == 0:
        print(number + " is even")
    else:
        print(number + " is odd")

def F2():
    number1 = input("Enter a number: ")
    while number1.isnumeric() == False:
        number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")
    while number2.isnumeric() == False:
        number2 = input("Enter another number: ")
    if number1 > number2 :
        print(number1 + " is bigger!")
    elif number1 < number2 :
        print(number2 + " is bigger!")
    elif number1 == number2:
        print(number1 + " and " + number2 + " are the same!")
        



