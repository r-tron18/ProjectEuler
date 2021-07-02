

def ispalindrome(num):
    dig = str(num)
    ln = len(dig)
    for i in range(ln//2):
        if dig[i] != dig[ln-i-1]:
            return False

    return True

ans = 0
for n1 in range(100, 1000):
    for n2 in range(n1, 1000):
        pro  = n1 * n2
        if ispalindrome(pro):
            ans = max(ans, pro)

print(ans)
            
