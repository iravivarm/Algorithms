A=[24,5,6,10,28,32]
# print(max(A))
# max_num=max(A)

# count=0
# for num in A:
#     if num == max_num:
#         count=count+1

# print(count)
# print (len(A)-count)

max=A[0]
count=1
for num in range(1,len(A)):
    if A[num] > max:
        max=A[num]
    elif A[num]==max:
        count = count + 1
print(count)
out=len(A)-count
print(out)
