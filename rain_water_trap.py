A=[0,1,0,2]

trap_water=0
n=len(A)
left_max=[0]*n
right_max=[0]*n
left_max[0]=A[0]
right_max[n-1]=A[n-1]


for i in range(1,n):
    left_max[i]=max(left_max[i-1],A[i])

for j in range(n-2,-1,-1):
    right_max[j]=max(right_max[j+1],A[j])

for k in range(n):
    trap_water += min(left_max[k], right_max[k])-A[k]

print(trap_water)