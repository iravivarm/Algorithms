def solve(A, B):
    for i in range(len(A)):
        print(A[i])
        for j in range(i+1, len(A)):
            # print(j)
            if A[i] + A[j] == B:
                return 1
    return 0

A=[1,2,3,4]
B=9

print(solve(A,B))