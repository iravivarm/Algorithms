A = [3, 6, 8, 10, 15, 50]
B = 5

####################Brute Force#####

# count=0
# for i in range(len(A)):
#     for j in range(i+1,len(A)):
#         if A[i] ^ A[j] == B:
#             count += 1

##############using dictonairies#########

count=0
hm={}

for i in A:
    target=B^i
    if target in hm:
        count = count+1
    else:
        hm[i]=i
print(count)
    