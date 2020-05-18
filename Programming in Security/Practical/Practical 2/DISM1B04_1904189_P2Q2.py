number1 = int(input("Pls enter a starting number: "))
number2 = int(input("Pls enter an ending number: "))
output = ""

if number1 < number2:
    while number1 != number2:
        if number1 % 2 == 1:
            output += str(number1) + "\t"
        number1 += 1
    print(output)

elif number2 < number1:
    while number1 != number2:
        if number1 % 2 == 1:
            output += str(number1) + "\t"
        number1 -= 1
    print(output)
        
else:
    print("The two numbers are the same")


