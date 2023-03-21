
def fib(A):
    if A<=1:
        return A
    # if A==1:
    #     return 1
    return fib(A-1) + fib(A-2)

def solve(A):
    return fib(A)

print(solve(9))


# def fib(A):
#     if A==0:
#         return 0
#     if A ==1:
#         return 1
#     return fib(A-1) + fib(A-2)

# def solve(A):
#     return fib(A)

# print(solve(9))