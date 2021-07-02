
pri = {}

def isprime(num):
    if num==2 or num==3:
        return True

    div = 3
    while div**2 <= num:
        if num%div==0:
            return False
        div+=2

    return True

primeCount = 1
limit = 10001
n = 3
while True:
    if isprime(n):
        primeCount += 1
    if primeCount == limit:
        print(n)
        break
    n+=2
