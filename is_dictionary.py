def is_dictonary(A,B):
    b_dict={val:i for i,val in enumerate(B)}
    print(b_dict)
    char_index=[b_dict.get(i[0]) for i in A if i[0] in b_dict]
    print(char_index)
    for num in range(1,len(char_index)):
        if char_index[num-1]>char_index[num]:
            return 0
    return 1




A =[ "ipial", "qjqgt", "vfnue", "vjqfp", "eghva", "ufaeo", "atyqz", "chmxy", "ccvgv", "ghtow" ]
B = "nbpfhmirzqxsjwdoveuacykltg"

print(is_dictonary(A,B))
