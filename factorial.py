def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact


def combination(n, m):
    value = factorial(n)/(factorial(n-m)*factorial(m))
    return int(value)


def pascal(r):
    lst = []
    for i in range(0, r+1):
        lst.append(combination(r, i))
    return lst


print(pascal(2))
