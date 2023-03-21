# B = 8   
# A = [3, 5, 1, 2, 1, 2]
A_dict={}

def check_sum_pair(B,A):
    B_dict={}
    for num in range(len(B)):
        if B[num] in B_dict:
            B_dict[B[num]] += 1
        else:
            B_dict[B[num]] = 1


    for i in range(len(B)):
        target=A-B[i]
        # print(target)

        if target == B[i] :
            # return (target, i)
            if B_dict[B[i]] >=2 :
                    return i, B_dict[target]
        elif target in B_dict:
            if B_dict[B[i]] >=1 :
                    return i, B_dict[target]
    return 0

nums = [3,4,2]
target = 5
print(check_sum_pair(nums, target))