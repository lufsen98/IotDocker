import socket

def connect_to_server(host,port):
    #create a socket object using ipv4 and TCP protokoll
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect to server
    client_socket.connect((host,port))

    #recive data from server
    data = client_socket.recv(1024) #buffer size 1024 bytes
    print("Recived from server:", data.decode()) # decode bytes to string

    # close the socket
    client_socket.close()

#connect to the server with local host ip and port 12345
connect_to_server ('localhost',8080)
