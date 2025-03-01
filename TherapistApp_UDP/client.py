import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 12349)

    # Send an initial message
    print("Welcome to the therapy session! Type 'exit' to end.")

    while True:
        # Get user input
        message = input("You: ")
        client.sendto(message.encode(), server_address)

        if message.lower() == "exit":
            response, _ = client.recvfrom(1024)
            print(response.decode())
            break

        # Receive therapist's response
        response, _ = client.recvfrom(1024)
        print(f"Therapist: {response.decode()}")

    client.close()

if __name__ == "__main__":
    start_client()
