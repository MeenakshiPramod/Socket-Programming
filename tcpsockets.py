import socket
import sys
try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP socket
except socket.error as e:
    print("Failed to create a socket.")
    print("Reason"+str(e))
    sys.exit(1)
print("Socket created.")

target_host = input("Enter the target_host name to connect: ")
target_port = int(input("Enter the target_port number : "))
try:
    sock.connect((target_host,int(target_port)))
    print("Socket connected to "+target_host+" on port "+str(target_port))
    sock.shutdown(2)
except socket.error as e:
    print("Failed to connect "+target_host+target_port)
    print("Reason"+str(e))
    sys.exit(1)