
def solve(n):
    return (n * (n+1) * (3*n**2 - n - 2)) // 12

N = 100
ans = solve(N)
print(ans)
