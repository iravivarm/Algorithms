A = [2,3, 4]

def gcd(A,B):
    while A>0:
        rem=B%A
        B=A
        A=rem
    return B

print(gcd(120,270))
ans=0
for i in range(len(A)):
    ans=gcd(ans,A[i])
print(ans)

