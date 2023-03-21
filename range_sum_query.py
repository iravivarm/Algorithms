def pf_range_sum(A,B):
    pf_sum=[]
    pf_range_sum=[]
    for i in range(0,len(A)):
        if i == 0:
            pf_sum.append(A[0])
        else:
            pf_sum.append(pf_sum[i-1]+A[i])
    
    for i in range(0,len(B)):
        start=B[i][0]-1
        end=B[i][1]-1
        if i == 0:
            pf_range_sum.append(pf_sum[end])
        else:
            pf_range_sum.append(pf_sum[end] - pf_sum[start - 1])
     
    return pf_range_sum


A = [2, 2, 2]
B = [[1, 1], [2, 3]]

print(pf_range_sum(A,B))