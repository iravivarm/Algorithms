def solve(A,B,C):
    return pow(A,B,C)
def pow(A,B,C):
    if B==0:
        return 1%C
    if B ==1:
        return A%C
    pow_value=(pow(A,B//2,C))%C

    if B%2==1:
        return((pow_value*pow_value)%C * A)%C
    return (pow_value*pow_value)%C
    

A = 2
B = 3
C = 3

print(solve(A,B,C))
