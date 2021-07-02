from math import factorial

def solve(n):
    fact = factorial(n)
    ans = 0
    while fact:
        ans += fact%10
        fact = fact//10

    return ans

print(solve(100))
