A= [
    [1, 2],
    [3, 4]
 ]

rev_matrix=[]
transpose_mat = [[A[col][row] for col in range(len(A))] for row in range(len(A[0]))]
print(transpose_mat)
for i in range(len(transpose_mat)):
    rev_matrix.append(transpose_mat[i][::-1])

print(rev_matrix)