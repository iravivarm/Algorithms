A=[0,1,2,0,1,2]

# for i in range(len(A)):
#     for j in range(i+1, len(A)):
#         if A[i] >= A[j]:
#             A[i],A[j] = A[j],A[i]

# print(A)

n=len(A)
count_0=0
count_1=0 
count_2=0
count_fre=[]
for i in A:
    if i == 0:
        count_0 += 1
    if i == 1: count_1 +=1
    if i == 2: count_2 += 1

count_fre=[0]*count_0 + [1] * count_1 + [2] * count_2

print(count_fre)