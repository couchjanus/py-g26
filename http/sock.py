
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
HOST = '127.0.0.1'
PORT = 4000

# with server as s:
server.bind((HOST, PORT))
server.listen()

while True:
    con, addr = server.accept()
    print('Connected by: ', addr)

    # with con:
    #     print('Connected by: ', addr)
    #     print("IP-address: ", addr[0])
    #     print("IP-port: ", addr[1])
    
    while True:
        data = con.recv(1024)
        if not data:
            break
        con.sendall(data)
    con.close()
    
# server.close()

