import socket
def getnewsocket():
	return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket = getnewsocket()
host = "localhost"
clientsocket.connect((host, 8089))	
while True:
    msg = input("msg to send ['q' to quit; 'x' to quit and stop the server]=>")    
    obuf = msg.encode() # convert msg string to bytes
    ret=clientsocket.send(obuf)
    #print("{} byte(s) have sent".format(ret))
    if (msg == 'q' or msg == 'x'):
        clientsocket.close()
        break  
    else:
        ibuf = clientsocket.recv(255)
        if len(ibuf) > 0:
            print(ibuf.decode())
        else:
            print("The connection has dropped")
            break
print("Bye Bye")
