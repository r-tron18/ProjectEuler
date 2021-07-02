
def get(num, k):
    n = num//k
    return (n * (n+1) * k) // 2

n = 999
sum3 = get(n, 3)
sum5 = get(n, 5)
sum15 = get(n, 15)

ans = sum3 + sum5 - sum15
print(ans)
