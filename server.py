import socket
import threading

clients = {}  # store client sockets with their names

def handle_client(conn, addr):
    name = conn.recv(1024).decode().strip()
    clients[conn] = name
    print(f"{name} connected from {addr}")
    broadcast(f"{name} joined the chat!", conn)

    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"{name}: {msg}")
            broadcast(f"{name}: {msg}", conn)
        except:
            break

    conn.close()
    del clients[conn]
    broadcast(f"{name} left the chat.", conn)


def broadcast(message, sender_conn):
    for client in list(clients.keys()):
        if client != sender_conn:
            try:
                client.send(message.encode())
            except:
                client.close()
                del clients[client]


def main():
    host = "0.0.0.0"
    port = 5000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    main()
