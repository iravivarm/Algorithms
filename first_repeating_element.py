A = [6, 10, 5, 4, 9, 120]
def first_repeating_elemet(A):
    A_dict={}
    for i in A:
        if i in A_dict:
            A_dict[i]+=1
        else:
            A_dict[i]=1

    print(A_dict)

    for i in A_dict:
        if A_dict.get(i) > 1:
            return i
    return -1

print(first_repeating_elemet(A))