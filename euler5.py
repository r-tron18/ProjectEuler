from math import gcd

def _lcm(a, b):
    return a*b // gcd(a, b)

def Lcm(li: list) -> int :
    lcm = 1
    for it in li:
        lcm = _lcm(it, lcm)
    return lcm
    
