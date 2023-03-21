A=[16,17,4,3,5,2]

n=len(A)
leader=[A[n-1]]

# leaders=[]

for i in range(n-2,-1,-1):
    if A[i] > leader[-1]:
        leader.append(A[i])
print(leader)
