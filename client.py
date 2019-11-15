import socket
from alphaPrime import AlphaPrime
from Encrypt import DES

HOST = '127.0.0.1'
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
    print(prime, a)

    message = input("enter code: ")
    while message != 'quit':
        client.sendall(message.encode("utf-8"))
        try:
            if serverCode and clientCode:
                yFirst = (a**serverCode) % prime
                ySecond = (a**clientCode) % prime
                key = (ySecond**serverCode) % prime 
                print('Key :' + repr(key))
                msg = input('Enter message: ')
                des = DES().encrypt(msg, str(key))
                message = des

            elif isPrime(message):
                clientCode = int(message)
                print('Waiting code from server.')
                data = client.recv(BUFSIZE)
                
                if clientCode and isPrime(data.decode('utf-8')):
                    print('Received secret code: ' + data.decode('utf-8'))
                    serverCode = int(data.decode('utf-8'))
                elif data:
                    print('False secret code!')
                else:
                    break


        except Exception as e:
            print(e)
            clientCode = None
        if not serverCode:
            message = input("enter code: ")


    client.close()
