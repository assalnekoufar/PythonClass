def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact


def combination(n, m):
    value = 0
    value = factorial(n)/factorial(n-m)*factorial(m)
    return int(value)

n = int(input("please enter your n number--->"))
m = int(input("please enter your m number--->"))
print(combination(n, m))
