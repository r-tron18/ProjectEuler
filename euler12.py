def primeFact(n: int) -> dict:

    dic = {}
    if n%2==0:
        c = 0
        while n%2==0:
            c += 1
            n = n//2

        dic[2] = c

    div = 3
    while div**2 <= n:
        if n%div==0:
            c = 0
            while n%div == 0:
                n = n//div
                c += 1
            dic[div] = c

        div += 2

    if n>2:
        dic[n] = 1

    return dic

n = 1
while True:
    tnum = n * (n+1) // 2
    d = primeFact(tnum)

    pr = 1
    for v in d.values():
        pr *= v+1
    if pr> 500:
        print(tnum)
        break

    n+=1
