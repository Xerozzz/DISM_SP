def Q1():
    open_ports = input("Please enter ports that were found to be open '|' ")
    open_ports = open_ports.replace(" ",'')
    open_ports = open_ports.split(sep='|')

    port_to_check = input("Please enter port number for your 'service' ")
   #for count in range(0,len(open_ports)):
    for count in open_ports:
        if count == port_to_check:
            print(f'Yes, port {port_to_check} is open!')
            break
    else:
        print(f'Sorry, port {port_to_check} is closed!')

def Q2():
    s = input("Please enter your restaurant dishes, separated by comma ',' \n")
    dishes = s.split(sep=',')
    
    choice = input("Please input food to search: ")
    matches = ""

    for dish in dishes:
        if dish.lower().find(choice.lower()) >= 0:
            matches+="\n" + dish.strip()

    if len(matches) > 0:
        print(f'Yes, we serve the following: {matches}')
    else:
        print(f'Sorry, we dont serve {choice}!\nPlease choose from {dishes}')

def Q3():
    marks = [80,39,79,81,79,70,84,57,66,86]
    print(f'Scores that qualify for "A" grade are:')
    for i in marks:
        if i > 79:
            print(i)
    count=0
    marks_failed = "Index(es) of students who failed: "
    while count < len(marks):
        if marks[count] < 50:
            marks_failed += f"{count} "
        count += 1
    marks_ascending = sorted(marks)
    marks_descending = sorted(marks,reverse=True)
    marks_max = max(marks)
    marks_min = min(marks)
    print(f'Marks in ascending order : {marks_ascending}')
    print(f'Marks in desscending order : {marks_descending}')
    print(f'Highest mark : {marks_max}')
    print(f'Lowest mark : {marks_min}')
    print(marks_failed)


