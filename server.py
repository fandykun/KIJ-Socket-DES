import socket
import threading
from alphaPrime import AlphaPrime
from DES import DES

HOST = ''
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

    socket.close()

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
    

if __name__ == "__main__":    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print('Waiting for a connection')
    connection, client_address = server.accept()

    clientCode = None
    serverCode = None
    prime = 97
    a = AlphaPrime().findPrimitive(prime)

    print('Connection from: ', client_address)
    while not serverCode or not clientCode:
        data = connection.recv(BUFSIZE)

        # Jika belum mendapat secret code
        if not clientCode:
            print('Received secret code: ' + data.decode('utf-8'))
            clientCode = int(data.decode('utf-8'))
            secret =  int(input('input code: '))
            message = str((a**secret) % prime)
            try:
                serverCode = int(message)
            except:
                serverCode = None
            connection.send(message.encode('utf-8'))   

        elif data:
            print('False secret code!')
        else:
            break
    
    key = (clientCode**secret) % prime
    receive = threading.Thread(target=receiveMessage, args=(connection, key))
    send = threading.Thread(target=sendMessage, args=(connection, key))
    
    receive.start()
    send.start()
    send.join()
    receive.join()

    # connection.close()
    # server.close()