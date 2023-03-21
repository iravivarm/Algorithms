A=[3, 4, 3, 6, 6]
def unique_ele_freq(A):
    frq=0
    A_dict={}

    for i in range(len(A)):
        if A[i] in A_dict:
            A_dict[A[i]] += 1
        else:
            A_dict[A[i]] = 1

    for i in A_dict:
        if A_dict.get(i) == 1:
            frq += 1
    return frq

print(unique_ele_freq(A))