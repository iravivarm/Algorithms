def solve(A):
    return factorial(A)

def factorial(A):
    if A==0:
        return 1
    return factorial(A-1)*A


print(solve(4))

