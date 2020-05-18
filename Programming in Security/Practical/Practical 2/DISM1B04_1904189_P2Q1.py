total=0
average=0
number=0
count=0

number = input("Pls enter a number or Q to stop: ")
while number.isnumeric() == False and number != "Q":
    number = input("Pls enter a number or Q to stop: ")
while number != "Q":
    total += int(number)
    print("Current total of " + str(count) + " values is " + str(total))
    count += 1
    number = input("Pls enter a number or Q to stop: ")
    while number.isnumeric() == False and number != "Q":
        number = input("Pls enter a number or Q to stop: ")

average = round((total/count),2)  #Need to make it to round off to 2 decimal places
print("Average of " + str(count) + " numbers is " + str(average))
    
    
