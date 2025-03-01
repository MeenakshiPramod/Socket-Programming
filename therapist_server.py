import socket
import threading
import random

# Predefined therapist responses
responses = [
    "Tell me more about that.",
    "How does that make you feel?",
    "Why do you think that happened?",
    "Can you elaborate on that?",
    "What do you think is the next step?",
    "That sounds interesting. Please go on.",
    "Have you discussed this with anyone else?",
    "What would you like to achieve from this?",
    "Let's explore that further.",
    "How long have you been feeling this way?",
]

def handle_client(client_socket):
    client_socket.send("Welcome to the therapy session! How can I help you today?".encode())

    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode()
            if message.lower() == "exit":
                print("Client ended the session.")
                client_socket.send("Goodbye! Take care.".encode())
                break

            # Respond with a random therapist message
            response = random.choice(responses)
            client_socket.send(response.encode())
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12349))  # Use a different port
    server.listen(5)
    print("Therapist server started. Waiting for clients...")

    while True:
        client_socket, client_address = server.accept()
        print(f"New connection from {client_address}")

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()