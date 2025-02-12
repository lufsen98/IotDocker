import socket 

def start_server(host,port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host,port))
    server_socket.listen(1)
    print(f"server listening on {host}:{port}")
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    message = "hello, client! This is a TCP server."
    client_socket.send(message.encode())

    client_socket.close()

    server_socket.close()

    start_server('localhost',12345)
