A = [2, 2, 2]
B = [[1, 1], [2, 3]]


sum_list=[]
for num in B:
    sum_arr=A[num[0]-1:num[1]]
    sum_range=sum(sum_arr)
    sum_list.append(sum_range)


print(sum_list)  