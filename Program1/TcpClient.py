import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))
payload='Hey Server'

try:
    while True:
        client_socket.send(payload.encode('utf-8'))
        data = client_socket.recv(1024)
        print(str(data))
        more=input('Want to send more data to the server: ')
        if more.lower() == 'yes':
            payload=input("Enter the payload: ")
        else:
            break
except KeyboardInterrupt:
    print('Exited by the user')
client_socket.close()
