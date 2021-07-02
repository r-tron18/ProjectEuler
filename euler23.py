from r_std import sigma
from collections import defaultdict as dd

dic = dd(int)

abundant = []

for i in range(1, 28124):
    if sigma(i) > 2*i:
        abundant.append(i)

ln = len(abundant)
for i in range(ln):
    for j in range(i, ln):
        val =  abundant[i] + abundant[j]
        dic[val] = 1


for i in range(1, 28
