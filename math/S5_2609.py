def gcd(a,b):
    r = a%b
    if r == 0:
        return b
    else:
        return gcd(b,r)

def lcm(a, b, g):
    return a*b//g

a, b = map(int, input().split())
g = gcd(a,b)
l = lcm(a,b,g)
print(g)
print(l)