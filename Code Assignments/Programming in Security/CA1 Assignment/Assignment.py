#Advanced Features
#- User System + Disount
#- Changing menu items based on day
#- Admin add items to menu
#- File System
#- Quiz for discount
#- Donation Fund :D
#- Delete item from cart
#- Feedback System
#- Guest User

#Importing required modules
import math,random,datetime,sys

#To create the food objects
class Food:
    def __init__(self,name,price):
        self.name = name
        self.price = price

#For USER objects
class User:
    def __init__(self,username,password,discount):
        self.username = username
        self.password = password
        self.discount = discount

#Guest User
guest = User("Guest","Guest","0")
    
#Find out what day is today and create menu
def WhatDayIsIt():
    import datetime
    datetime.datetime.today()
    datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
    global today
    today = datetime.datetime.today().weekday()

#Create the menu of the day
menu = []
def CreateMenu():
    WhatDayIsIt()
    #For fixed menu
    f = open("Assignment/menus/fixed.txt")
    for line in f:
        line = (line.strip()).split(sep=",") #Create parameters
        create = Food(line[0],line[1]) #Creates the Food item
        menu.append(create)
    f.close()
    #For daily menu
    f = open("Assignment/menus/" + str(today) +".txt")
    for line in f:
        line = (line.strip()).split(sep=",") #Create parameters
        create = Food(line[0],line[1]) #Creates the Food item
        menu.append(create)
    f.close()

#Creates User database
users=[]
def CreateUsers():
    f = open("Assignment/menus/users.txt")
    for line in f:
        line = (line.strip()).split(sep=",") #Create parameters
        create = User(line[0],line[1],line[2]) #Creates the useritem
        users.append(create)
    f.close()
#For users to log in/guest login

def Login():
    CreateUsers()
    correct_username = False
    while correct_username == False:
        username_entered = input("Please enter your username: ")
        for i in users:
            if (i.username).lower() == username_entered.lower():
                global account_logged_in
                account_logged_in = i
                print(f'Account found!')
                correct_username = True
                break
        else:
            print("Account not found!")
    correct_password = False
    while correct_password == False:
        password_entered = input("Please enter your password: ")
        if password_entered.lower() == account_logged_in.password:
            print("Password correct! Login successful!")
            correct_password = True
        else:
            print("Incorrect password! Please try again!")

#Create a new account
def CreateNewUser():
    new_name = input("Enter your username: ")
    new_password = input("Enter your password: ")
    f = open("Assignment/menus/users.txt","a")
    f.write("\n" + new_name + "," + new_password + ",0")
    f.close()
    print("Account created! Please log in!")

#Display menu
def displayMenu():
    count = 1
    print("Today's menu!\n===============\n")
    for i in menu:
        print(f'{count}. {i.name}\t${i.price}')
        count += 1
    input("Press ENTER to continue...\n") 

#Search Item/Add
def Search():
    searchbar = []
    to_search = input("Please enter the name of food to search or press ENTER to see all: ")
    
    for food in menu:
        if (food.name).lower().find(to_search.lower()) >= 0:
            searchbar.append(food)
    if len(searchbar) > 0:
        print(f'Yes, we serve the following: ')
        count = 1
        for i in searchbar:
            print(f'{count}. {i.name}\t${i.price}')
            count += 1
        selection = input("Enter the item number of the dish that you would like to order, or 0 to stop: ")
        while selection != "0":
            try:
                selection = int(selection) - 1
                cart.append(searchbar[selection])
                print(f'{searchbar[selection].name} was added!')
            except:
                print("Invalid input! Please try again.")
            selection = input("Enter the item number of the dish that you would like to order, or 0 to stop: ")
    else:
        print(f'Sorry, we dont serve {to_search}!\nPlease view the menu!')

#To display cart
def displayCart():
    print('\n======================\nThis is your current cart!\n')
    count = 1
    for i in cart:
        print(f'{count}. {i.name}\t${i.price}')
        count += 1
    s = input("Press the number of the item you want to delete or press ENTER to continue...") 
    if s == "":
        pass
    try:
        s = int(s) - 1
        deleted = cart[s]
        cart.remove(deleted)
        print(f'{deleted.name} has been removed from cart!')
    except:
        print("Invalid input! Try again!")

#Donation
def Donate():
    f = open("Assignment/menus/donate.txt")
    current_donation = f.read()
    print(f"Thank you for choosing to donate! Current total donated amount is ${current_donation}!")
    f.close()
    global donate_fund
    donate_fund = input("How much would you be willing to donate?\n$")
    s = False
    while s == False:
        try:
            donate_fund = float(donate_fund)
            s = True
        except:
            donate_fund = input("Invalid input!\n")
    f = open("Assignment/menus/donate.txt","w")
    f.write(str(int(current_donation) + donate_fund))
    f.close()
    print("Thank you for your donation!")

#Feedback
def Feedback():
    feedback = input("Please give your feedback:\n")
    f = open("Assignment/menus/feedback.txt","a")
    f.write(f'\n{feedback}')
    f.close()
    print("Thank you for your feedback!")

#To check out
cost=0
payment = 0
def Checkout():
    for i in cart:  
        global cost,payment
        cost += float(i.price)
    valid = False
    discount = 0
    global donate_fund
    donate_fund = 0
    s = input("Do you want to attempt a quiz to get a discount? (y/n)\n")
    while s.lower() != "y" and s.lower() != "n" :
        s = input("Enter 'y' or 'n' only please!\n")
    if s == "y":
        correctAnswers = 0
        print("Welcome to the quiz! For each question you get correct, you get a 10 percent discount! You only get one try each so make sure to not mis-enter your answers!")
        first_answer = input("========================\nWhat is 9+8?\n\n1. 12\n2. 38\n3. 89\n4. 17\n")
        if first_answer == "4":
            print("Correct answer!")
            correctAnswers += 1
        else: 
            print("Wrong answer!")
        second_answer = input("========================\nWhat is 8x4?\n\n1. 10\n2. 32\n3. 1\n4. 23\n")
        if  second_answer == "2":
            print("Correct answer!")
            correctAnswers += 1
        else: 
            print("Wrong answer!")
        third_answer = input("========================\nWhat is 98-23?\n\n1. 72\n2. 75\n3. 23\n4. 11\n")
        if third_answer == "2":
            print("Correct answer!")
            correctAnswers += 1
        else: 
            print("Wrong answer!")
        discount = (10 * correctAnswers) + int(account_logged_in.discount)
    donate = input("Would you like to donate some money to the SPAM Charity? (y/n)\n")
    while donate.lower() != "y" and donate.lower() != "n" :
        donate = input("Enter 'y' or 'n' only please!\n")
    if donate == "y":
        Donate()
    print(f"Total cost of your order: ${round(cost,2)}")
    print(f'Discount: {str(discount)}%')
    cost = round((cost/100)*(100-int(discount)),2)
    cost += donate_fund
    print(f'Final price: ${cost} (inclusive of donation if any)')
    while valid == False:
        try:
            payment = float(input("Please enter your payment: $"))
            valid = True
        except:
            print("INVALID INPUT")
    s = False
    while s == False:
        if payment == cost:
            print("You have paid in exact! Thank you!")
            s= True
        elif payment > cost:
            change = payment - cost
            print(f'Your change is ${round(change,2)}. Thank you!')
            s = True
        elif payment < cost:
            print(f'Thats too little! Come back when you have more money!')
            payment = float(input(f"Try again!\n"))
    s = input("Do you want to give us feedback for improvement? (y/n)\n")
    while s.lower() != "y" and s.lower() != "n" :
        s = input("Enter 'y' or 'n' only please!\n")
    if s == "y":
        Feedback()

#Admin System
def admin():
    choice = 0
    while choice !="":
        choice = input("==========================\nAdmin System\n==========================\n1. Add item to fixed menu\n2. Press ENTER to exit the program\n")
        while choice != "1" and choice !="":
            choice = input("Invalid Input!\n")
        if choice == "1":
            food_name = input("Input name of food item: ")
            food_name = food_name.strip()
            food_price = input("Input price of food item: ")
            s = False
            while s == False:
                try:
                    food_price = float(food_price)
                    s = True
                    food_price = str(food_price)
                except:
                    food_price = input("Invalid input!\n")
            food_price = food_price.strip()
            f= open("Assignment/menus/fixed.txt","a")
            f.write(f"\n{food_name},{food_price}")
            f.close()
            print(f'Item added!')

global current_account
cart = []
#Actual Application
def Program():
    #Prepares menu
    global account_logged_in
    CreateMenu()
    print(f'=================\nWelcome to SPAM!\n=================\n\nFirsty, do you have an account?')
    choice = input("1. Log in\n2. Create New Account\n3. Guest Login\n")
    while choice != "1" and choice != "2" and choice != "3":
        choice = input('Invalid Option! Please try again!\n')
    if choice == "1":
        Login()
    elif choice == "2":
        CreateNewUser()
        Login()
    elif choice == "3":
        account_logged_in = guest
    print("Thank you!")
    print(f'Logged in as user: {account_logged_in.username}!\nPlease choose your option')
    if account_logged_in.username == "admin":
        admin()
    else:
        while choice != "":
            choice = input("==========================\n1. Display Today's Menu\n2. Add Item to Cart/Search Menu\n3. Delete Item from Cart/Display cart\n4. Check out\nENTER to exit\n")
            while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "":
                choice = input('Invalid Option! Please try again!\n')
            if choice == "1":
                displayMenu()
            elif choice == "2":
                Search()
            elif choice == "3":
                displayCart()   
            elif choice == "4":
                Checkout()
                break
    print('Thank you for using SPAM! Goodbye!')

Program()