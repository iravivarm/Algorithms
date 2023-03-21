A = [4, 7, 9 ]
B = [2, 11, 19 ]

def merge(A,B):
    n=len(A)
    m= len(B)

    C= [0]*(n+m)
    A_pointer=0
    B_pointer=0
    C_pointer=0
    while A_pointer < n and B_pointer < m:
        if A[A_pointer] <= B[B_pointer]:
            C[C_pointer]=A[A_pointer]
            A_pointer +=1
            C_pointer += 1
        else:
            C[C_pointer]=B[B_pointer]
            B_pointer += 1
            C_pointer += 1
    while A_pointer < n:
        C[C_pointer] = A[A_pointer]
        A_pointer+= 1
        C_pointer += 1
    while B_pointer < m:
        C[C_pointer] = B[B_pointer]
        B_pointer += 1
        C_pointer += 1
    return C

print(merge(A,B))