A=236
def colorful_num(A):
    A_set=set()
    prod=1
    list_A=list(str(A))
    n=len(list_A)


    for i in range(n):
        for j in range(i,n):
            prod=1
            for k in range(i, j+1):
                prod = prod * int(list_A[k])
            if prod not in A_set:
                A_set.add(prod)
            else: 
                 return 0 
    return 1


print(colorful_num(A))



