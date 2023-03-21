A = [5, 15,30]

def gcd(A,B):
    while A>0:
        rem=B%A
        B=A
        A=rem
    return B
n=len(A)
left_gcd = [0] * (n)
left_gcd[0] = A[0]
prev = A[0]
for i in range(1,len(A)):
    left_gcd[i] = gcd(prev,A[i])
    prev = left_gcd[i]
    
# **Creating Suffix GCD  Array**
right_gcd = [0] * (n)
right_gcd[-1] = A[-1]
prev = A[-1]
for j in range(n-1,-1,-1):
    right_gcd[j] = gcd(prev,A[j])
    prev = right_gcd[j]
    
ans = float('-inf')

for k in range(n):
    if k == 0:
        value = right_gcd[k+1]
    elif k == n-1:
        value = left_gcd[k-1]
    else:
        value = gcd(left_gcd[k-1],right_gcd[k+1])
    
    ans = max(ans,value)
print(ans) 