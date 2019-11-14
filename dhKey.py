from bigPrime import BigPrime
from alphaPrime import AlphaPrime

def key():
    bigPrime = BigPrime().generatePrimeNumber(40)
    alphaPrime = AlphaPrime().findPrimitive(bigPrime)

    prime = bigPrime
    a = alphaPrime

    print(prime)
    print(a)
    firstNumber = 97
    secondNumber = 233
    yFirst = (a**firstNumber) % prime
    ySecond = (a**secondNumber) % prime
    kFirst = (ySecond**firstNumber) % prime
    kSecond = (yFirst**secondNumber) % prime

    print(kFirst)
    print(kSecond)

