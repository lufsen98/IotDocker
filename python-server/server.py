import socket 

def start_server(host, port):
    #create a socket object using ipv4 and TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind the socket to the address and port
    server_socket.bind(host,port))

    #Enable the server to accept connections, with 1 client in the waiting que 
    server.socket.listen(1)
    print(f"Server listeing on {host}:{port}")

    #wait for a client connection
    client_socket, addr = server_socket.accept()
    print(f"connection from {addr}")

    # send a message to the connected client
    message = "Hello, client! This is a TCP server."
    client_socket.send(message.encode()) #encode string to bytes
    print(f"Connection from {addr}")

    #Close the client socket
    client_socket.close()

    # close the server socket
    server_socket.close()

#start the server  with local host IP and port 12345
start_server('127.0.0.1', 123)





