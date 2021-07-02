
mx_chain = 1
number = 1
dic = {1:1}

def itera(num):
    global mx_chain
    global number
    
    li = []
    while num!=1 and dic.get(num, 0)==0:
        li.append(num)
        if num%2:
            num = 3*num + 1
        else:
            num = num//2
            
    prev = num
    while li:
        nm = li.pop()
        dic[nm] = dic[prev] + 1
        if mx_chain < dic[nm]:
            mx_chain = dic[nm]
            number = nm
        prev = nm
n = 2
limit = 10**6
while n < limit:
    itera(n)
    n+=1

print(number)
