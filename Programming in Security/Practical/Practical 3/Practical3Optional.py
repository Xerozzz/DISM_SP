def Q2():
    s = input("Please enter your restaurant dishes, separated by comma ',' \n")
    dishes = s.split(sep=',')
    
    choice = 0
    while choice != "":
        choice = input("Please input food to search: ")
        matches = ""

        for dish in dishes:
            if dish.lower().find(choice.lower()) >= 0:
                matches+="\n" + dish.strip()

        if len(matches) > 0:
            print(f'Yes, we serve the following: {matches}')
        else:
            print(f'Sorry, we dont serve {choice}!\nPlease choose from {dishes}')
