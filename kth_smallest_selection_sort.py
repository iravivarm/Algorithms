A=[2,1,4,3,2]
B=3
def selection_sort(A,B):
    print(type(A))
    for i in range(B):
        min_value=A[i]
        index=i
        for j in range(i, len(A)):
            if A[j] < min_value:
                min_value =A[j]
                index = j
        A[i],A[index] = A[index],A[i]
        # temp=A[i]
        # A[i]=A[index]
        # A[index]=temp
    print(A)
    return A[B]

print(selection_sort(A,B))

# for i in range(len(A)):
#     for j in range(i, len(A)):
#         print(i,j)