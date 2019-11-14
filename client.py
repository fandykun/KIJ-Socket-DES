import socket

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except:
    print('Connection error')
    exit()

print("Enter 'quit' to exit")
message = input(" -> ")

while message != 'quit':
    client.sendall(message.encode("utf-8"))
    message = input(" -> ")
    data = client.recv(1024, ).decode('utf-8')
    print('Data received: ' + data)

client.close()


