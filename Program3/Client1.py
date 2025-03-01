import socket

client_socket=socket.socket()

host="127.0.0.1"
port=1233

print("Waiting for connection")
try:
    client_socket.connect((host,port))
except socket.error as e:
    print(str(e))

Response=client_socket.recv(1024)
print(Response.decode('utf-8'))

while True:
    Input=input("Say something: ")
    client_socket.send(str.encode(Input))
    response=client_socket.recv(1024)
    print("Server response: ", response.decode('utf-8'))