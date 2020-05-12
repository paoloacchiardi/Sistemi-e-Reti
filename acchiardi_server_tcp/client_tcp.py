import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',2000)) #connetto il client al server dandogli indirizzo e porta del server
while(True):
    mex = input("Inserisci una stringa:\t")
    s.sendall(mex.encode()) #trasformo da string a bin
    if(mex == "shutdown"):
        break
    data = s.recv(4096)
    print(data.decode()) #trasformo da bin a string
s.close()