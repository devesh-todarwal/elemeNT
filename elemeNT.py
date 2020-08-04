'''
Functions implemented are:
		1. gcd(a,b) - Compute the greatest common divisor of a and b.
		2. Xgcd(a,b) - (Extended Euclid Algorithm) Find [g,x,y] such that g=gcd(a,b) and g = ax + by.
		3. power_mod(b,e,n) - Compute b^e mod n efficiently.
		4. inverse_mod(b,n) - Compute 1/b mod n (Doesn't always exist).
		5. is_prime(n) - Test whether n is prime using a variety of pseudoprime tests.
		6. euler_criterion(a, p) - Test whether a is a quadratic residue mod p
		7. euler_phi(n) - Compute Euler's Phi function of n - the number of integers strictly less than n which are coprime to n.
		8. carmichael_lambda(n) - Compute Carmichael's Lambda function of n - the smallest exponent e such that b**e = 1 for all b coprime to n.
		9. factor(n) - Return a sorted list of the prime factors of n with exponents.
		10. prime_divisors(n) - Returns a sorted list of the prime divisors of n.
		11. is_primitive_root(g,n) - Test whether g is primitive - generates the group of units mod n.
		12. sqrtmod(a,n) - Compute sqrt(a) mod n using various algorithms.
		13. TSsqrtmod(a,grpord,n) - Compute sqrt(a) mod n using Tonelli-Shanks (RESSOL) algorithm.
		14. isprimeF(n,b) - Test whether n is prime or a Fermat pseudoprime to base b.
		15. isprimeE(n,b) - Test whether n is prime or an Euler pseudoprime to base b.
		16. factorone(n) - Find a factor of n using a variety of methods.
		17. factors(n) - Return a sorted list of the prime factors of n. (Prior to ver 0.7 named factor(n))
		18. factorPR(n) - Find a factor of n using the Pollard Rho method.
'''

import math
import functools
def manual():
	print("***Welcome to elemeNT: An elementary Number Theoretic Library***\n")
	print("The available functions are: \n")
	print("1. gcd(a,b) - Compute the greatest common divisor of a and b.\n")
	print("2. Xgcd(a,b) - Find [g,x,y] such that g=gcd(a,b) and g = ax + by.\n")
	print("3. power_mod(b,e,n) - Compute b^e mod n efficiently.\n")
	print("4. inverse_mod(b,n) - Compute 1/b mod n.\n")
	print("5. is_prime(n) - Test whether n is prime using a variety of pseudoprime tests.\n")
	print("6. euler_criterion(a, p) - Test whether a is a quadratic residue mod p.\n")
	print("7. euler_phi(n) - Compute Euler's Phi function of n - the number of integers strictly less than n which are coprime to n.\n")
	print("8. carmichael_lambda(n) - Compute Carmichael's Lambda function of n - the smallest exponent e such that b**e = 1 for all b coprime to n.\n")
	print("9. factor(n) - Return a sorted list of the prime factors of n with exponents.\n")
	print("10. prime_divisors(n) - Returns a sorted list of the prime divisors of n.\n")
	print("11. is_primitive_root(g,n) - Test whether g is primitive - generates the group of units mod n.\n")
	print("12. sqrtmod(a,n) - Compute sqrt(a) mod n using various algorithms.\n")
	print("13. TSsqrtmod(a,group_ord,n) - Compute sqrt(a) mod n using Tonelli-Shanks (RESSOL) algorithm.\n")
	print("14. isprimeF(n,b) - Test whether n is prime or a Fermat pseudoprime to base b.\n")
	print("15. isprimeE(n,b) - Test whether n is prime or an Euler pseudoprime to base b.\n")
	print("16. factorone(n) - Find a factor of n using a variety of methods.\n")
	print("17. factors(n) - Return a sorted list of the prime factors of n.\n")
	print("18. factorPR(n) - Find a factor of n using the Pollard Rho method.\n")

### DEFINITIONS BEGIN HERE ###

def euler_criterion(a, p):
    """p is odd prime, a is positive integer. Euler's Criterion will check if
	a is a quadratic residue mod p. If yes, returns True. If a is a non-residue
	mod p, then False"""
    return pow(a, (p - 1) // 2, p) == 1

def gcd(a,b):
	"""gcd(a,b) returns the greatest common divisor of the integers a and b."""
	a = abs(a); b = abs(b)
	while (a > 0):
		b = b % a
		tmp=a; a=b; b=tmp
	return b

def Xgcd(a,b):
	"""Xgcd(a,b) returns a tuple of form (g,x,y), where g is gcd(a,b) and
	x,y satisfy the linear equation g = ax + by."""
	a1=1; b1=0; a2=0; b2=1; aneg=1; bneg=1
	if(a < 0):
		a = -a; aneg=-1
	if(b < 0):
		b = -b; bneg=-1
	while (1):
		quot = -(a // b)
		a = a % b
		a1 = a1 + quot*a2; b1 = b1 + quot*b2
		if(a == 0):
			return (b, a2*aneg, b2*bneg)
		quot = -(b // a)
		b = b % a;
		a2 = a2 + quot*a1; b2 = b2 + quot*b1
		if(b == 0):
			return (a, a1*aneg, b1*bneg)

def power_mod(b,e,n):
	"""power_mod(b,e,n) computes the eth power of b mod n.
	(Actually, this is not needed, as pow(b,e,n) does the same thing for positive integers.
	This will be useful in future for non-integers or inverses.)"""
	if e<0: # Negative powers can be computed if gcd(b,n)=1
		e = -e
		b = inverse_mod(b,n)
	accum = 1; i = 0; bpow2 = b
	while ((e>>i)>0):
		if((e>>i) & 1):
			accum = (accum*bpow2) % n
		bpow2 = (bpow2*bpow2) % n
		i+=1
	return accum

def inverse_mod(a,n):
	"""inverse_mod(b,n) - Compute 1/b mod n."""
	(g,xa,xb) = Xgcd(a,n)
	if(g != 1): raise ValueError("***** Error *****: {0} has no inverse (mod {1}) as their gcd is {2}, not 1.".format(a,n,g))
	return xa % n

def is_prime(n):
	"""is_prime(n) - Test whether n is prime using a variety of pseudoprime tests."""
	if n<0: n=-n  # Only deal with positive integers
	if n<2: return False # 0 and 1 are not prime
	if (n in (2,3,5,7,11,13,17,19,23,29)): return True
	return isprimeE(n,2) and isprimeE(n,3) and isprimeE(n,5)

def factor(n):
	"""factor(n) - Return a sorted list of the prime factors of n with exponents."""
	# Rewritten to align with SAGE.  Previous semantics available as factors(n).
	if ((abs(n) == 1) or (n == 0)): raise ValueError('Unable to factor {0}'.format(n))
	factspow = []
	currfact = None
	thecount = 1
	for thefact in factors(n):
		if thefact != currfact:
			if currfact != None:
				factspow += [(currfact,thecount)]
			currfact = thefact
			thecount = 1
		else:
			thecount += 1
	factspow += [(thefact,thecount)]
	return tuple(factspow)

def prime_divisors(n):
	"""prime_divisors(n) - Returns a sorted list of the prime divisors of n."""
	return tuple(set(factors(n)))

def euler_phi(n):
	"""euler_phi(n) - Computer Euler's Phi function of n - the number of integers
	strictly less than n which are coprime to n.  Otherwise defined as the order
	of the group of integers mod n."""
	if n == 1: return 1
	if n <= 0: return 0
	# For each prime factor p with multiplicity n, a factor of (p**(n-1))*(p-1)
	return functools.reduce(lambda a,x:a*(x[0]**(x[1]-1))*(x[0]-1),factor(n),1)

def carmichael_lambda(n):
	"""carmichael_lambda(n) - Compute Carmichael's Lambda function
	of n - the smallest exponent e such that b**e = 1 for all b coprime to n.
	Otherwise defined as the exponent of the group of integers mod n."""
	# SAGE equivalent is sage.crypto.util.carmichael_lambda(n)
	if n == 1: return 1
	if n <= 0: raise ValueError("*** Error ***:  Input n for carmichael_lambda(n) must be a positive integer.")
	# The gcd of (p**(e-1))*(p-1) for each prime factor p with multiplicity e (exception is p=2).
	def _carmichael_lambda_primepow(theprime,thepow):
		if ((theprime == 2) and (thepow >= 3)):
			return (2**(thepow-2)) # Z_(2**e) is not cyclic for e>=3
		else:
			return (theprime-1)*(theprime**(thepow-1))
	return functools.reduce(lambda accum,x:(accum*x)//gcd(accum,x),tuple(_carmichael_lambda_primepow(*primepow) for primepow in factor(n)),1)

def is_primitive_root(g,n):
	"""is_primitive_root(g,n) - Test whether g is primitive - generates the group of units mod n."""
	# SAGE equivalent is mod(g,n).is_primitive_root() in IntegerMod class
	if gcd(g,n) != 1: return False  # Not in the group of units
	order = euler_phi(n)
	if carmichael_lambda(n) != order: return False # Group of units isn't cyclic
	orderfacts = prime_divisors(order)
	for fact in orderfacts:
		if pow(g,order//fact,n) == 1: return False
	return True

def sqrtmod(a,n):
	"""sqrtmod(a,n) - Compute sqrt(a) mod n using various algorithms.
	Currently n must be prime, but will be extended to general n (when I get the time)."""
	# SAGE equivalent is mod(g,n).sqrt() in IntegerMod class
	if(not isprime(n)): raise ValueError("*** Error ***:  Currently can only compute sqrtmod(a,n) for prime n.")
	if(pow(a,(n-1)//2,n)!=1): raise ValueError("*** Error ***:  a is not quadratic residue, so sqrtmod(a,n) has no answer.")
	return TSsqrtmod(a,n-1,n)

def TSsqrtmod(a,grpord,p):
	"""TSsqrtmod(a,grpord,p) - Compute sqrt(a) mod n using Tonelli-Shanks (RESSOL) algorithm.
	Here integers mod n must form a cyclic group of order grpord."""
	# Rewrite group order as non2*(2^pow2)
	ordpow2=0; non2=grpord
	while(not ((non2&0x01)==1)):
		ordpow2+=1; non2//=2
	# Find 2-primitive g (i.e. non-QR)
	for g in range(2,grpord-1):
		if (pow(g,grpord//2,p)!=1):
			break
	g = pow(g,non2,p)
	# Tweak a by appropriate power of g, so result is (2^ordpow2)-residue
	gpow=0; atweak=a
	for pow2 in range(0,ordpow2+1):
		if(pow(atweak,non2*2**(ordpow2-pow2),p)!=1):
			gpow+=2**(pow2-1)
			atweak = (atweak * pow(g,2**(pow2-1),p)) % p
			# Assert: atweak now is (2**pow2)-residue
	# Now a*(g**powg) is in cyclic group of odd order non2 - can sqrt directly
	d = invmod(2,non2)
	tmp = pow(a*pow(g,gpow,p),d,p)  # sqrt(a*(g**gpow))
	return (tmp*inverse_mod(pow(g,gpow//2,p),p)) % p  # sqrt(a*(g**gpow))//g**(gpow//2)

def isprimeF(n,b):
	"""isprimeF(n) - Test whether n is prime or a Fermat pseudoprime to base b."""
	return (pow(b,n-1,n) == 1)

def isprimeE(n,b):
	"""isprimeE(n) - Test whether n is prime or an Euler pseudoprime to base b."""
	if (not isprimeF(n,b)): return False
	r = n-1
	while (r % 2 == 0): r //= 2
	c = pow(b,r,n)
	if (c == 1): return True
	while (1):
		if (c == 1): return False
		if (c == n-1): return True
		c = pow(c,2,n)

def factorone(n):
	"""factorone(n) - Find a prime factor of n using a variety of methods."""
	if (is_prime(n)): return n
	for fact in (2,3,5,7,11,13,17,19,23,29):
		if n%fact == 0: return fact
	return factorPR(n)  # Needs work - no guarantee that a prime factor will be returned

def factors(n):
	"""factors(n) - Return a sorted list of the prime factors of n. (Prior to ver 0.7 named factor(n))"""
	if n<0: n=-n  # Only deal with positive integers
	if (is_prime(n)):
		return [n]
	fact = factorone(n)
	if ((abs(n) == 1) or (n == 0)): raise ValueError('Unable to factor \"{0}\"'.format(n))
	facts = factors(n//fact) + factors(fact)
	facts.sort()
	return facts

def factorPR(n):
	"""factorPR(n) - Find a factor of n using the Pollard Rho method.
	Note: This method will occasionally fail."""
	numsteps=2*math.floor(math.sqrt(math.sqrt(n)))
	for additive in range(1,5):
		fast=slow=1; i=1
		while i<numsteps:
			slow = (slow*slow + additive) % n
			i = i + 1
			fast = (fast*fast + additive) % n
			fast = (fast*fast + additive) % n
			g = gcd(fast-slow,n)
			if (g != 1):
				if (g == n):
					break
				else:
					return g
	return 1