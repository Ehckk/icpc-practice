a, b = map(int, input().split())

def gcd(a,b):
    
    if a == 0:
        return b

    return gcd(b%a, a)

print(gcd(a,b))