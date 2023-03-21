def solve(A, B):
    res_list= []
    count = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            count += 1
            A[i] = count
        else:
            A[i] = count
    print(A)
    
    for i in range(len(B)):
        left = B[i][0]
        right = B[i][1]
        if left == 0:
            res_list.append(A[right])
        else:
            res_list.append(A[right]-A[left-1])    
    return res_list

A = [1, 2, 3, 4, 5]
B = [   [0, 2], 
        [2, 4],
        [1, 4] ,  ]
print(solve(A,B))