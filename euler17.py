o = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
     6:'six', 7:'seven', 8:'eight', 9:'nine'}
t1 = {0:'', 10:'ten', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
      60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
t2 = {11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
      16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

def ones(num):
    num = int(num)
    return o[num]

def twos(num):
    num = int(num)
    
    if 10 < num < 20:
        return  t2[num]

    a, b = num//10, num%10
    if num<10:
        return ones(b)
    
    ans = t1[a*10]
    if b:
        ans += ' ' + ones(b)
    return ans

def three(num):
    st = str(num)
    ans = ones(st[0]) + ' hundred'
    if num%100:
        ans += ' and ' + twos(st[1:])

    return ans

def solve():
    ans = 0
    
    for i in range(1, 10):
        w = ones(i)
        ans += len(w)

    for i in range(10, 100):
        w = twos(i).split(' ')
        for it in w:
            ans += len(it)

    for i in range(100, 1000):
        w = three(i).split(' ')
        for it in w:
            ans += len(it)

    ans += 11
    #print('one thousand')

    return ans
