import socket
def connect_to_server(host,port):
    # create a client socket. Socket is built by IPV4 ip adress and TCP PROTOKOLL(SOCK_STREAM)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #now that we have create a client socket. we want to connect to it
    #can only connect to sockets
    client_socket.connect((host,port))
    # client recive data from server in data variabl
    data = client_socket.recv(1024) #Buffer size how large amount of datat that can be recieved.
    #printout the data recived from server.
    print("Data recieved from server: ", data.encode())
    
    client_socket.close()
#send data to socket. 
connect_to_server('localhost',8080)

