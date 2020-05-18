total=0
number=0

number = input("Pls enter a number or Q to stop: ")
while number.isnumeric() == False:
    number = input("Pls enter a number or Q to stop: ")
while number != "Q":
    total += int(number)
    print("Current total is " + str(total))
    number = input("Pls enter a number or Q to stop: ")
    while number.isnumeric() == False and number != "Q":
        number = input("Pls enter a number or Q to stop: ")

print("Final sum is " + str(total))
