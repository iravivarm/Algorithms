def gcd(A,B):
    while A>0:
        rem=B%A
        B=A
        A=rem
    return B

print(gcd(4,6))