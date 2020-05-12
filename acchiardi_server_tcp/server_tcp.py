import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET = ipv4, SOCK_STREAM = tcp
s.bind(('localhost',2000))
s.listen()
conn,address = s.accept()
while(True):
    data = conn.recv(4096)
    if(data.decode() == "shutdown"): #decode() rende da bin a string
        break
    conn.sendall(data)
conn.close()
s.close()