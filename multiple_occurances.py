def count_occurances(arr, search_num):
    numCount=0
    for num in arr:

        if arr[num]==search_num:
            numCount += 1
    return numCount

A = [1, 2, 2]

print(count_occurances(A,3))

