A=[-7,1,5,2,-4,3,0]


def equillibrium_index(A):
    left_sum, right_sum=0, sum(A)

    for idx,num in enumerate(A):
        right_sum = right_sum - num
        if left_sum == right_sum:
            return idx
        left_sum = left_sum + num
    return -1

print(equillibrium_index(A))