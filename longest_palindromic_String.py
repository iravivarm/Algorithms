A = "aaaabaaa"
n=len(A)
def pallindrome_index(l,r):
    while (l>=0 and r < len(A) and A[l]==A[r]):
        l=l-1
        r=r+1
    return(A[l+1:r])

res=''
for i in range(len(A)):
    odd=pallindrome_index(i,i)
    if len(odd) > len(res):
        res=odd
    even=pallindrome_index(i,i+1)
    if len(even) > len(res):
        res=even
print(res)

    