import socket,pickle
#Find out what day is today and create menu
def WhatDayIsIt():
    import datetime
    datetime.datetime.today()
    datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
    global today
    today = datetime.datetime.today().weekday()

#Food class
class Food:
    def __init__(self,name,price):
        self.name = name
        self.price = price

#Creates menu
def chooseMenu(serversocket):
    WhatDayIsIt()
    #For fixed menu
    menu = []
    f = open("menus/fixed.txt")
    for line in f:
        line = (line.strip()).split(sep=",") #Create parameters
        create = Food(line[0],line[1]) #Creates the Food item
        menu.append(create)
    f.close()
    #For daily menu
    f = open("menus/" + str(today) +".txt")
    for line in f:
        line = (line.strip()).split(sep=",") #Create parameters
        create = Food(line[0],line[1]) #Creates the Food item
        menu.append(create)
    f.close()
    return menu
    
#simServer can hanlde muliple echo request from the client,
#but it only handles one client at a time.
def handler(con):
    buf = con.recv(255) # buf is of the type of byte
    if len(buf) > 0:
        if buf == b"menu": #To send menu
            print("Menu sent!")
            menu = chooseMenu(serversocket)
            con.send(pickle.dumps(menu))
            return ''
        elif buf == b"feedback":    #To enter feedback
            print("Requesting for feedback input")
            con.send("getfeedback".encode())
            feedback = con.recv(4096).decode()
            print("Feedback received!")
            f = open("menus/feedback.txt","a")
            f.write(f'\n{feedback}')
            f.close()
            con.send("Feedback lOgged!".encode())
            return ''
        elif buf == b'transaction':
            print("Requesting for transaction input")
            con.send("gettransaction".encode())
            transaction = pickle.loads(con.recv(4096))
            print("Transaction Log Received!")
            f = open("menus/transactionlogs.txt","a")
            from datetime import date
            today = date.today()
            f.write(f'{today}:\n{transaction}\n')
            return 'x'
    else: # 0 length buf implies client has dropped the con.
        return ""  # quit this handler immediately and return ""  
    con.close() #exit from the loop when client sent q or x
    return buf.decode()
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8089))
serversocket.listen()
while True:
    print("waiting a new call at accept()")
    connection, address = serversocket.accept()
    if handler(connection) == 'x':
        break
serversocket.close()
print("Server stops")

