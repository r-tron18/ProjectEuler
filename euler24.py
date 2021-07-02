from math import factorial

def find_lexo(li, position):
    if position < 1:
        print('Not Possible')
        return

    position -= 1
    ln = len(li)-1
    ans = ''
    while position:
        f = factorial(ln)
        ind = position//f
        ans += li.pop(ind)

        position -= f*ind
        ln-=1

    ans += ''.join(li)

    return ans

li = [str(i) for i in range(10)]
print(li)
print(find_lexo(li, 10**6))
