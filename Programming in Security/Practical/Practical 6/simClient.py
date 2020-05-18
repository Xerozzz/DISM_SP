import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)host = "localhost"
clientsocket.connect((host, 8089))  
while True:
    msg = input("msg to send ['q' to quit; 'x' to quit and stop the server]=>")
    obuf = msg.encode() # convert msg string to bytes
    ret=clientsocket.send(obuf)

    if (msg == 'q' or msg == 'x'):
        clientsocket.close()
        break  
    else:
        ibuf = clientsocket.recv(255)
        if len(ibuf) > 0:
            print(ibuf.decode())
        else:
            print("The connection has dropped")
            break
print("Bye Bye")
