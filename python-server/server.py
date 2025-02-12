import socket

def start_server(host, port):
    # Create a socket object using IPv4 and TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Enable the server to accept connections, with 1 client in the waiting queue
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    # Wait for a client connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    
    # Send a message to the connected client
    message = "Hello, client! This is a TCP server."
    client_socket.send(message.encode())  # Encode string to bytes
    
    # Close the client socket
    client_socket.close()
    
    # Close the server socket
    server_socket.close()

# Start the server with local host IP and port 12345
start_server('0.0.0.0', 8080)
