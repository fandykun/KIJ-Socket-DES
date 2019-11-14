# Python3 program to find primitive root 
# of a given number n 
from math import sqrt 

class AlphaPrime:
	def __init__(self):
		pass

	def isPrime(self, n) -> bool:
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

	def power(self, x, y, p) -> int:
		""" Iterative Function to calculate (x^n)%p 
		in O(logy) """	
		res = 1 # Initialize result 

		x = x % p # Update x if it is more 
				# than or equal to p 

		while (y > 0): 

			# If y is odd, multiply x with result 
			if (y & 1): 
				res = (res * x) % p 

			# y must be even now 
			y = y >> 1 # y = y/2 
			x = (x * x) % p 

		return res 		


	def findPrimefactors(self, s, n):
	# Utility function to store prime 
	# factors of a number 
	
		# Pr the number of 2s that divide n 
		while (n % 2 == 0) : 
			s.add(2) 
			n = n // 2

		# n must be odd at this po. So we can 
		# skip one element (Note i = i +2) 
		for i in range(3, int(sqrt(n)), 2): 
			
			# While i divides n, pr i and divide n 
			while (n % i == 0) : 

				s.add(i) 
				n = n // i 
			
		# This condition is to handle the case 
		# when n is a prime number greater than 2 
		if (n > 2) : 
			s.add(n) 

	def findPrimitive(self, n) -> int:
	# Function to find smallest primitive 
	# root of n 
		s = set() 

		# Check if n is prime or not 
		if (self.isPrime(n) == False): 
			return -1

		# Find value of Euler Totient function 
		# of n. Since n is a prime number, the 
		# value of Euler Totient function is n-1 
		# as there are n-1 relatively prime numbers. 
		phi = n - 1

		# Find prime factors of phi and store in a set 
		self.findPrimefactors(s, phi) 

		# Check for every number from 2 to phi 
		for r in range(2, phi + 1): 

			# Iterate through all prime factors of phi. 
			# and check if we found a power with value 1 
			flag = False
			for it in s: 

				# Check if r^((phi)/primefactors) 
				# mod n is 1 or not 
				if (self.power(r, phi // it, n) == 1): 

					flag = True
					break
				
			# If there was no power with value 1. 
			if (flag == False): 
				return r 

		# If no primitive root found 
		return -1
