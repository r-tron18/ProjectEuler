
with open('euler18_data', 'r') as fil:
    dat = fil.read().split('\n')
    if dat[-1] == '':
        dat = dat[:-1]

    li = [list(map(int, st.split(' '))) for st in dat]
    

for ind in range(len(li)-1, 0, -1):
    lis = []
    for i in range(len(li[ind])-1):
        d = max(li[ind][i], li[ind][i+1])
        lis.append(d)

    for i, it in enumerate(li[ind-1]):
        li[ind-1][i] = it + lis[i]

print(li[0])
    
