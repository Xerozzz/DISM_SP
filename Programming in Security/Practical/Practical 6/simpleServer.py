import socket
#simServer can hanlde muliple echo request from the client,
#but it only handles one client at a time.
def handler(con):
    while True:
        buf = con.recv(255) # buf is of the type of byte
        if len(buf) > 0:
            print(buf.decode())  # decode with system default encoding scheme
            if buf == b"q" or buf == b"x":
                break
            else:
                # echo back the same byte sequence to client
                con.sendall(buf)
        else: # 0 length buf implies client has dropped the con.
            return ""  # quit this handler immediately and return ""  
    con.close() #exit from the loop when client sent q or x
    return buf.decode()
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections
while True:
    print("waiting a new call at accept()")
    connection, address = serversocket.accept()
    if handler(connection) == 'x':
        break; 
serversocket.close()
print("Server stops")
