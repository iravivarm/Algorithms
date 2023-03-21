A = [   [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]   ]
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]


rows=len(A)
columns=len(A[0])
pf_sum=[[0]*columns for row in range(rows)]


###Buildinf the the pf_matrix
###Row-wise
for row in range(rows):
    sum=0
    for col in range(columns):
        sum += A[row][col]
        pf_sum[row][col]=sum
print(pf_sum)
## Col-wise from the pf_sum
for col in range(columns):
    sum=0
    for row in range(rows):
        sum += pf_sum[row][col]
        pf_sum[row][col]=sum
print(pf_sum)





