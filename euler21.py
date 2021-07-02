def get_divs_sum(n):
    sm = 0
    for d1 in range(1, int(pow(n, 0.5))+1):
        if n%d1 == 0:
            d2 = n//d1
            sm+=d1
            if d1!=d2:
                sm += d2
    return sm-n

dic = {}
def d(n):
    if n in dic:
        return dic[n]
    val = get_divs_sum(n)
    dic[n] = val
    return val

def solve(n):
    S = set()
    for i in range(1, n+1):
        b = d(i)
        if i!=b and d(b)==i:
            S.add(i)
            if b <= n:
                S.add(b)

    return sum(S)

