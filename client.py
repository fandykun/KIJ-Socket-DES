import socket
import threading
from alphaPrime import AlphaPrime
from DES import DES

HOST = '127.0.0.1'
PORT = 12345
BUFSIZE = 64

def receiveMessage(socket, key):
    des = DES()
    start = True
    while start:
        message = socket.recv(BUFSIZE)
        if message == b'':
            start = False
        else:
            print('Received message: ' + message.decode('utf-8'))
            decrypt = des.decrypt(message.decode('utf-8'), str(key))
            print('Decrypt message: ' + decrypt)
    

def sendMessage(socket, key):
    des = DES()
    start = True
    while start:
        message = input('enter message: ')
        if message == 'quit':
            start = False
        else:
            encrypt = des.encrypt(message, str(key))
            socket.send(encrypt.encode('utf-8'))
    
    socket.close()

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except:
        print('Connection error')
        exit()
    print("Enter 'quit' to exit")
    
    clientCode = None
    serverCode = None
    prime = 97
    a = AlphaPrime().findPrimitive(prime)

    secret = int(input("enter code: "))
    message = str((a**secret) % prime)
    while not serverCode or not clientCode:
        client.sendall(message.encode("utf-8"))

        clientCode = int(message)
        print('Waiting code from server.')
        data = client.recv(BUFSIZE)
        
        if clientCode:
            print('Received secret code: ' + data.decode('utf-8'))
            serverCode = int(data.decode('utf-8'))
        elif data:
            print('False secret code!')
        else:
            break

    key = (serverCode**secret) % prime
    send = threading.Thread(target=sendMessage, args=(client, key))
    receive = threading.Thread(target=receiveMessage, args=(client, key))
    
    send.start()
    receive.start()
    receive.join()
    send.join()


    # client.close()
