import sys
try:
    years=int(input("Enter  number of years in service: "))
except ValueError:
    print("You did not enter a number!")
    sys.exit()
    
try:
    salary=int(input("Enter current salary: $"))
except ValueError:
    print("You did not enter a number!")
    sys.exit()

increment=0
if years < 10:
    if salary < 1000:
        increment = 100
        
    elif salary < 2000:
        increment = 200
        
    elif salary >= 2000:
        increment = 300
        
elif years > 9:
    if salary < 1000:
        increment = 200
        
    elif salary < 2000:
        increment = 300

    elif salary >= 2000:
        increment = 400

print("Your increment is " + str(increment))
