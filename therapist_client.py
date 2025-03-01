import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12349))

    # Receive the welcome message
    print(client.recv(1024).decode())

    while True:
        # Send a message to the therapist
        message = input("You: ")
        client.send(message.encode())

        if message.lower() == "exit":
            print(client.recv(1024).decode())
            break

        # Receive the therapist's response
        response = client.recv(1024).decode()
        print(f"Therapist: {response}")

    client.close()

if __name__ == "__main__":
    start_client()