def find_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return "is not a prime number"
        return "is a prime number"


print(find_prime_number(3))
