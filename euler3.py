

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
                
                
