import random
import math


def find_prime_number(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return "is not a prime number"
        return "is a prime number"


lst_1 = [random.randint(2, 10000) for i in range(1, 1000)]

primes = [n1 for n1 in lst_1 if find_prime_number(n1) == "is a prime number"]
print(primes)

