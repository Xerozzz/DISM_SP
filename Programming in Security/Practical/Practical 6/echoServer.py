# very primitive echo server
# It runs forever till receiving a byte of 'x' is recevied.
# echo one and only one mesg for each connected client. 
import socket 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8089)) # 0.0.0.0 is a special address
print("Server starts listening ...")
serversocket.listen(5)

while True:
    con, address = serversocket.accept()
    print("got a new connection.. waiting for mesg now...")
    # Got one client connection establish
    buf = con.recv(255)
    if len(buf) > 0:    # may get a zero len buf (when the con has dropped)  
        print(buf.decode())      # buf is in byte type
        if buf == b"x": # compare buf in byte type
            # recevie a special msg. Quit the server
            con.close()
            break
        else:
            # echo back to client
            con.sendall(buf)
            con.close() # always disconnect after one echo. go back to listen.
serversocket.close()
print("Server has stopped")
