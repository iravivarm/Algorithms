A=4
B=3



ans=0
power=0

while A>0:
    rem=A%B
    ans = ans + rem * (10 ** power)
    power = power + 1
    print(A//=B)
    A//=B



print(ans) 