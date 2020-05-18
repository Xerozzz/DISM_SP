weight = int(input("Enter your weight : "))
height = float(input("Enter your height : "))
bmi = str(round((weight/height)/height,1))
print("Your BMi is " + bmi)