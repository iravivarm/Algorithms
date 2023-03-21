A=45

def solve(A):
    return sum_digits(0,A)

def sum_digits(sum_digit,A):
    print(A)
    if A>0:
        sum_digit += A%10
        return sum_digits(sum_digit,A//10)
    else:
        return sum_digit



print(solve(A))