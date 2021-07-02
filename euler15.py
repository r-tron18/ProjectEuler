

def solve():
    num = 1
    den = 1
    for i in range(20):
        num *= 40-i
        den *= 20-i

    return num//den

ans = solve()
print(ans)
