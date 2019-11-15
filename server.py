import socket
from alphaPrime import AlphaPrime
from Decrypt import DES

HOST = ''
PORT = 55555
BUFSIZE = 64

def isPrime(n) -> bool:
    try:
        n = int(n)
    except:
        return False
    # Corner cases 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True

    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0): 
        return False
    i = 5
    while(i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6

    return True

if __name__ == "__main__":    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))

    server.listen(1)

    print('Waiting for a connection')
    connection, client_address = server.accept()

    prime = 97
    a = AlphaPrime().findPrimitive(prime)
    print(prime, a)
    clientCode = None
    serverCode = None

    try:
        print('Connection from: ', client_address)

        while True:
            data = connection.recv(BUFSIZE)
            print(data.decode('utf-8'))

            # Jika data yang diterima bilangan prima,
            # maka dianggap sebagai secret code, server mengirim code juga untuk digenerate
            if isPrime(data.decode('utf-8')) and not clientCode:
                print('Received secret code: ' + data.decode('utf-8'))
                clientCode = int(data.decode('utf-8'))
                message =  input('input code: ')
                try:
                    if isPrime(message):
                        serverCode = int(message)
                except:     
                    serverCode = None
                connection.send(message.encode('utf-8'))   
            # Jika server dan client sudah saling menerima code bil.prima
            elif serverCode and clientCode and data:
                print('Received message: ' + data.decode('utf-8'))
                yFirst = (a**serverCode) % prime
                ySecond = (a**clientCode) % prime
                key = (yFirst**clientCode) % prime
                des = DES().decrypt(data.decode('utf-8'), str(key))
                print('Decrypt message: ' + des)

            elif data:
                print('False secret code!')
            else:
                break


    finally:
        print('Closing current connection')
        connection.close()

    server.close()