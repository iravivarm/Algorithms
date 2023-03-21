A=[1, 2, 3, 1, 2, 4]


# sums=0
# for i in range(len(A)):
#     sums = (sums^A[i])

# sums=(sums&-sums)

# unique_1=0
# unique_2=0
# for j in range(len(A)):
#         if(A[i]&sums) > 0:
#             unique_1^=A[i]
#             print(unique_1)
#         else:
#             unique_2^=A[i]
#             print(unique_2)


# if unique_1 > unique_2:
#     print(unique_2, unique_1)
# else:
#     print(unique_1,unique_2)



n=len(A)
sums=0
for i in range(n):
    sums^=(A[i])

print(sums)
sums=(sums & -sums) 
print(sums)           
unique_1,unique_2=0,0
for i in range(n):
    if(A[i]&sums) > 0:
        unique_1^=A[i]
    else:
        unique_2^=A[i]
if unique_1>unique_2:
    print(unique_2,unique_1)
else:
    print(unique_1,unique_2)