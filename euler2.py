
a, b  = 1, 2
sm = 0

while b < 4*10**6:
    sm += b
    for _ in range(3):
        a, b = b, a+b

print(sm)
