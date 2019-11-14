import socket
from des import DesKey
from alphaPrime import AlphaPrime

HOST = ''
PORT = 55555
BUFSIZE = 64

def isPrime(n) -> bool:
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

    clientCode = None
    serverCode = None
    try:
        print('Connection from: ', client_address)

        while True:
            data = connection.recv(BUFSIZE)

            # Jika server dan client sudah saling menerima code bil.prima
            if serverCode and clientCode:
                prime = 97
                a = AlphaPrime().findPrimitive(prime)
                yFirst = (a**serverCode) % prime
                ySecond = (a**clientCode) % prime
                kFirst = (ySecond**serverCode) % prime
                kSecond = (yFirst**clientCode) % prime
                

            # Jika data yang diterima bilangan prima,
            # maka dianggap sebagai secret code, server mengirim code juga untuk digenerate
            elif isPrime(int(data.decode('utf-8'))):
                print('Received secret code: ' + data.decode('utf-8'))
                clientCode = int(data.decode('utf-8'))
                serverCode = int(input('input code: '))
                connection.send(serverCode)   
            elif data:
                print('False secret code!')
            else:
                break

    finally:
        print('Closing current connection')
        connection.close()

    server.close()