A=[[1,2,3,4],
    [5,6,7,8],
    [9,2,3,4]]


def solve(A):
    rows_len=len(A)
    col_len=len(A[0])
    print(col_len)
    res=[]
    for row in range(0, rows_len):
        mat_sum=0
        for column in range(0, col_len):
            mat_sum=mat_sum+A[row][column]
            res.append(mat_sum)
    return res


print(solve(A))