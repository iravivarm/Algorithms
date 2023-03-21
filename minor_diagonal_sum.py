A = [[1, -2, -3],
      [-4, 5, -6],
      [-7, -8, 9]]



len_rows=len(A)
diag_sum=0

for row in range(len_rows):
	diag_sum = diag_sum + A[row][len_rows-row - 1]
print(diag_sum)