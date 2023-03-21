A = 9
B = 0
C = 7

def power_modulo(A,B,C):
    if A==0 or B==0 or C==0:
        return -1
    i=1
    ans=1
    while i<=B:
        ans=(ans%C * A%C)%C
        i +=1
    return ans%B

print(power_modulo(A,B,C))