number = input("Enter a number : ")
if number.isnumeric() == False :
    print("You did not enter a number")
else:
    if int(number) % 2 == 0:
        print(number + " is even")
    else:
        print(number + " is odd")
