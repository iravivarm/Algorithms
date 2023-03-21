A=[[1,2,3],
    [5,6,7],
    [9,2,3]]

row=len(A)
col=len(A[0])
diagonal_sum=0
for i in range(row):
	print(A[i][i])
	diagonal_sum = diagonal_sum + A[i][i]

print(diagonal_sum)