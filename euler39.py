
dic = {}

def doit(NUM):
    global ans
    global dic
    p = NUM//2
    Set = set()
    for m in range(1, p+1):
        for n in range(1, p+1):
            for k in range(1, p+1):
                if m*(m+n)*k > p:
                    break
                if m*(m+n)*k == p:
                    if m>n:
                        a = 2*m*n*k
                        b = (m**2 - n**2)*k
                        c = (m**2 + n**2)*k

                        a, b = min(a, b), max(a, b)
                        Set.add((a, b, c))

    return len(Set)

def solve(limit):
    mx = 0
    for i in range(2, limit+1, 2):
        a = doit(i)
        if a > mx:
            mx = a
            ans = i
            print(mx, ans)

    print(ans)  

solve(1000)

