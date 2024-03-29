from random import randrange, getrandbits

class BigPrime:
    def __init__(self):
        pass

    def isPrime(self, n, k) -> bool:
        """ Test if a number is prime
            Args:
                n -- int -- the number to test
                k -- int -- the number of tests to do
            return True if n is prime
        """
        # Test if n is not even.
        # But care, 2 is prime !
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        # find r and s
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        # do k tests
        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

    def generatePrimeCandidate(self, length) -> int:
        """ Generate an odd integer randomly
            Args:
                length -- int -- the length of the number to generate, in bits
            return a integer
        """
        # generate random bits
        p = getrandbits(length)
        # apply a mask to set MSB and LSB to 1
        p |= (1 << length - 1) | 1
        return p
    
    def generatePrimeNumber(self, length = 40) -> int:
        """ Generate a prime
            Args:
                length -- int -- length of the prime to generate, in          bits
            return a prime
        """
        p = 4
        # keep generating while the primality test fail
        while not self.isPrime(p, 128):
            p = self.generatePrimeCandidate(length)
        return p
