import sys
def sum_max_min_array(arr):
    max_num=-sys.maxsize-1
    min_num=sys.maxsize
    for num in range(0,len(arr)):
        if arr[num] > max_num:
            max_num = arr[num]
        if arr[num] < min_num:
            min_num = arr[num]
    return (max_num + min_num)


arr=[1,5,2,6,9]
print(solve(arr))