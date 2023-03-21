

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

M = len(A[0])
C = [[0] * len(A) for _ in range(M)]
print(M)

for row in range(len(A)):
    for col in range(row+1, len(A)):
        C[row][col]=A[col][row]
print(C)