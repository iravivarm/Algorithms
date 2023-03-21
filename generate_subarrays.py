A=[1,4,2,5,6]

arrs=[]
for i in range(len(A)):
    for j in range(i, len(A)):
        arrs.append(A[i:j+1])
print(arrs)