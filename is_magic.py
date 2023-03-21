def sum_digits(A):
    if A==0:
        return 0
    return sum_digits(A//10) + A%10


def solve(A):
    while A >=10:
        A=sum_digits(A)
    if A%9==1:
        return 1
    return 0

A = 83557

solve(83557)



A=83557

print(solve(A))