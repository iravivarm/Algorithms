strs = ["flower","flow","flight"]

fix_elem=strs[0][1]
print(fix_elem)



for i in range(1, len(strs)):
    com_prefix=""
    for j in range(len(strs[i])):
        if j<len(fix_elem) and fix_elem[j] == strs[i][j]:
            com_prefix += fix_elem[j]
        else: break
    fix_elem = com_prefix

print(fix_elem)


