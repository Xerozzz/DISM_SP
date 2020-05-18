#very basic client, at most send and receive one message.
import socket
def getnewsocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket = getnewsocket()
clientsocket.connect(('localhost', 8089))	
#only send one msg. 
msg = input("msg to send ['x' to shutdown server]=> ")
mbytes = msg.encode()     # encode unicode str to bytes before sending out
# For Python 3, type str is different from type byte
# have to encode the string to bytes. send() only works with bytes
clientsocket.send(mbytes)
if (msg != 'x'):
    # waiting for an echo reply 
    buf = clientsocket.recv(255)
    if len(buf) > 0:
        print(buf.decode()) # buf is byte, need decode before print as str.
clientsocket.close()