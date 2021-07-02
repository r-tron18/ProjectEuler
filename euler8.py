def pro(li):
    p = 1
    for it in li:
        p *= it
    return p

def hori(li, times):
    ans = 0
    for row in li:
        for i in range(len(row) - times + 1):
            ans = max(ans, pro(row[i:i+times]))  
    return ans

def vert(li, times):
    ans = 0
    for col in zip(*li):
        for i in range(len(col) - times + 1):
            if pro(col[i:i+times]) == 64497254400:
                print(col)
                print(col[i:i+times])
                print(i)
            ans = max(ans, pro(col[i:i+times]))
    return ans

def ldia(li, times):
    row = len(li)
    col = len(li[0])
    ans = 0
    for r in range(row-times+1):
        for c in range(col-times+1):
            pr = 1
            for i in range(times):
                pr*=li[r+i][c+i]
            ans = max(ans, pr)
    return ans

def rdia(li, times):
    row = len(li)
    col = len(li[0])
    ans = 0
    for r in range(row-times+1):
        for c in range(times-1, col):
            pr = 1
            for i in range(times):
                try:
                    pr*=li[r+i][c-i]
                except:
                    print(r, c, i)
                    input()
            ans = max(ans, pr)
    return ans

def solve(li, times):
    ans = hori(li, times)
    ans = max(vert(li, times), ans)
    ans = max(ldia(li, times), ans)
    ans = max(rdia(li, times), ans)
    return ans

with open('euler8_data', 'r') as fil:
    dat = fil.read()
    dat = dat.split('\n')
    dat = ''.join(dat)
    if dat[-1] == '':
        dat = dat[:-1]
    li = [list(map(int, list(st))) for st in dat]

ans = solve(li, 13)
print(ans)
