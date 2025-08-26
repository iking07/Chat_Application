import socket
import threading
import sys
import argparse

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(msg)
        except:
            print("Disconnected from server")
            sock.close()
            break

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--name", required=True)
    args = parser.parse_args()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((args.host, args.port))

    # send username first
    client.send(args.name.encode())

    print("Connected to server. You can start typing messages.")

    thread = threading.Thread(target=receive, args=(client,))
    thread.start()

    while True:
        msg = input()
        if msg == "/quit":
            client.close()
            sys.exit()
        client.send(msg.encode())

if __name__ == "__main__":
    main()
