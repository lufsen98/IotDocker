import socket

def start_server(host,port):
    #creates a socket for the server AF_INET ipv4 ip adresser, SOCK_STREAM vilket protokoll som ska användas när den tar emot och skickar data.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host,port)) # binder socketen till uppsättningen.

    server_socket.listen(1) # Lyssnar efter connections till socketen. kan ta emot en connection åt gången de andra nekas.
    print(f"Server listening on: {host}:{port}")


    client_socket, addr = server_socket.accept()
    print(server_socket)
    print(client_socket)
    print(f"Connections from {addr}")

    message = "Hello client,this is a TCP server"
    client_socket.send(message.encode())
    
    client_socket.close()

    server_socket.close()


start_server('127.0.0.1', 8080)

