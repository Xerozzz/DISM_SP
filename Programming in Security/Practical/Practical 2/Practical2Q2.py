import sys
number1 = input("Enter a number : ")
if number1.isnumeric() == False :
    print("You did not enter a number")
    sys.exit()
    
number2 = input("Enter a number : ")
if number2.isnumeric() == False :
    print("You did not enter a number")
    sys.exit()

if number1 > number2 :
    print(number1 + " is bigger!")
elif number1 < number2 :
    print(number2 + " is bigger!")
elif number1 == number2:
    print(number1 + " and " + number2 + " are the same!")
    
