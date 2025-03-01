import socket
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

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0.0.0.0', 12349))  # Use a different port
    print("Therapist UDP server started. Waiting for clients...")

    while True:
        try:
            # Receive message from the client
            message, client_address = server.recvfrom(1024)
            message = message.decode()

            if message.lower() == "exit":
                print(f"Client {client_address} ended the session.")
                server.sendto("Goodbye! Take care.".encode(), client_address)
                continue

            # Respond with a random therapist message
            response = random.choice(responses)
            server.sendto(response.encode(), client_address)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_server()
