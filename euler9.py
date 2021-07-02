

def solve():
    for m in range(1, 501):
        for n in range(1, 501):
            for k in range(1, 501):
                if m*(m+n)*k > 500:
                    break
                if m*(m+n)*k == 500:
                    if m-n>=1:
                        a = 2*m*n*k
                        b = (m**2 - n**2)*k
                        c = (m**2 + n**2)*k
                        print('debug a = {}, b = {}, c = {}'.format(a, b, c))
                        return a*b*c

print(solve())
