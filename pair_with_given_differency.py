A = [5, 10, 3, 2, 50, 80]
B = 78
def pair_with_diiference(A,B):
    hm={}
    for i in range(len(A)):
        if A[i] in hm:
            hm[A[i]] +=1
        else:
            hm[A[i]] = 1

    for i in A:
        if i - B in hm and B!=0:
            return 1
    return 0

print(pair_with_diiference(A,B))