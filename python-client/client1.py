import socket

def connect_to_server(host,port):
    client_socket = None
    try:
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        client_socket.settimeout(5)

        client_socket.connect((host,port))

        message = "Hello from python client\n"
        client_socket.send(message.encode())

        data = client_socket.recv(1024)

        print("Mottaget från server:", data.decode())

    except socket.timeout:
        print("Timeout: Kunde inte ansluta till servern")
    except ConnectionRefusedError:
        print("Anslutning nekad: Kontrollera att servern körs på rätt port")
    except Exception as e:
        print(f"ett fel uppstod: {e}")
    finally:
        if client_socket:
            client_socket.close()


if __name__ == "__main__":
    connect_to_server('localhost',8080)
