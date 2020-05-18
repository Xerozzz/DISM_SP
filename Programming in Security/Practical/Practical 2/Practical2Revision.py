def F1():
    try:
        number = int(input(f'Enter a number: '))
        if number % 2 == 0:
            print(f"{number} is even!")
        else: 
            print(f'{number} is odd!')
    except:
        print("NOT A NUMBER")

def F2():
    try:
        number = int(input("Enter first number: "))
        number2 = int(input("Enter second number: ")
        if number > number2:
            print(f'{number} is bigger.')
        elif number < number2:
            print(f'{number2} is bigger.')
        else:
            print(f'Both numbers are equal!')
    except:
        print("Not a number!")

def F3():
    try:
        number = int(input("Enter first number: "))
        number2 = int(input("Enter second number: ")
        sum = number + number2
        print(f'Sum of both numbers is {sum}')
    except:
        print("Not a number!")

def F4():
    