A=[ 8, 2, 5, 6, 7, 6, 2, 6, 2 ]
B=10

pow = 1
ans=0

for i in range(len(A)-1,-1,-1):
    print(i)
    ans=ans+(A[i]*pow)%B
    pow=(pow*10)%B



print(ans%B)