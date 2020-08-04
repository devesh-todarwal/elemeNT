# elemeNT: A Python Library with basic Number Theoretic Functions

## Purpose

In order to better understand the number theoretic functions learnt from the text of Thomas Koshy's Elementary Number Theory with Applications,
some of the key number theoretic functions were implemented in Python3. The methods include several prime factorisation techniques, modulo computation techniques and root computation techniques. 

## Usage

To use the library, just clone the repository in your source code's main folder and use the following in your script:
```
import elemeNT
```
And you are all set to go!

To understand more about the functions implemented use:

```
import elemeNT
elemeNT.manual()
```

## Implemented Functions (version - 1.0)
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
		13. TSsqrtmod(a,group_ord,n) - Compute sqrt(a) mod n using Tonelli-Shanks (RESSOL) algorithm.
		14. isprimeF(n,b) - Test whether n is prime or a Fermat pseudoprime to base b.
		15. isprimeE(n,b) - Test whether n is prime or an Euler pseudoprime to base b.
		16. factorone(n) - Find a factor of n using a variety of methods.
		17. factors(n) - Return a sorted list of the prime factors of n. (Prior to ver 0.7 named factor(n))
		18. factorPR(n) - Find a factor of n using the Pollard Rho method.
