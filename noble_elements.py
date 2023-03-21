def noble_element(A):
    A.sort()

    for i in len(A):
        if A[i] != A[i-1]:
            if A[i]==len(A)-1-i:
                    return 1
        if A[len(A)-1]==0: 
            return 1

        return -1    


