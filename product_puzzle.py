def solve(self, A):

    n=len(A)
    prod=1
    b=[]

    for i in range (0,n):  # iterating through the array and finding the product 
        prod=prod*A[i]
    
    for i in A:   # product is divided with each element of i 
        c=prod//i
        b.append(c)
    
    return b