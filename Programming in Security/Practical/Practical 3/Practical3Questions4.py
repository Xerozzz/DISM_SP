marks = [88,74,69,90,42,79,66,73,100,99]

def menu():
    choice = 0
    while choice != "":
        choice = input(f"Current marks for 10 students stored ins system.\n{marks}\n1. Entry of marks to MESS\n2. Display the max mark in the MESS\n3. Display the marks sorted in ascending order\n4. Display a subset of marks in the MESS\n")
        if choice == "1":
            entry()
        elif choice == "2":
            max_marks()
        elif choice == "3":
            sort_marks()
        elif choice == "4":
            edit_list()
    print('Thank you!')

def entry():
    global marks
    marks = []
    count = 1
    marks_entered=int(input(f'Please enter marks for student {count} or -1 to end: '))
    while marks_entered != -1:
        count += 1
        marks.append(marks_entered)
        marks_entered=int(input(f'Please enter marks for student {count} or -1 to end: '))

def max_marks():
    highest = max(marks)
    print(f'Highest Mark: {highest}')

def sort_marks():
    print(f'Marks in ascending order: {sorted(marks)}')

def edit_list():
    decision = int(input(f'The current set of marks stored in system is {marks}\nPlease choose how you want to edit the list: \n1. Slice the list\n2. Remove a mark from the list\n3. Change a mark\n4. Add new marks\n.Please choose how you want to edit the list: '))
    if decision == 1:
        splice()
    elif decision == 2:
        remove()
    elif decision == 3:
        change()
    elif decision == 4:
        add()

def splice():
    start = int(input(f'Input start index to subset: '))
    end = int(input(f'Input end index to subset: '))
    print(f'Your new marks set is {marks[start:end]}')

def remove():
    print(f'The current set of marks stored in system is {marks}')
    remove = int(input("Input index to remove: "))
    del marks[remove]
    print(marks)

def change():
    print(f'The current set of marks stored in system is {marks}')
    change = int(input("Input index to change: "))
    new_value= int(input("Input new value: "))
    marks[change] = new_value
    print(marks)

def add():
    print(f'The current set of marks stored in system is {marks}')
    new_value = int(input("Input new value: "))
    marks.append(new_value)
    print(marks)

menu()