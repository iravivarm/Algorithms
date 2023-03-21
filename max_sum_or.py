arr=[12,9]
k=1
max_num=0
# for i in range(len(arr)):
#     # print(arr[i]*2)
#     arr[i]=arr[i]*2**k
#     print("arr:",arr)
#     arr_sum=0
#     for num in range(len(arr)):
#         print(arr[num])
#         arr_sum=arr_sum | arr[num]
#         print(arr_sum)
#     if arr_sum > max_num:
#         max_num = arr_sum


# print(max_num)
def max_min_sum(arr,k):
    max_num=0

    if k <= 0:
        return -1
    
    
    for i in range(len(arr)):
        
        temp = arr[:]
        temp[i] =(temp[i])*2**k
        temp_sum=0
        for num in range(len(temp)):
            temp_sum=temp_sum | temp[num]
        if temp_sum>max_num:
            max_num = temp_sum
    return max_num


    for i in range(len(arr)):
        
        temp = arr[:]
        temp[i] =(temp[i])*2**k
        temp_sum=0
        for num in range(len(temp)):
            temp_sum=temp_sum | temp[num]
        if temp_sum>max_num:
            max_num = temp_sum
    return max_num

print(max_min_sum(arr,1))




