
def subarr_maxsum(arr):
    max_sum=0
    n=len(arr)
    if len(arr) <= 1:
        return arr[0] 
    
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum = sum + arr[j]
        
            if sum > max_sum:
                max_sum=sum
    return max_sum

arr=[2, 3, 4, -1, 6, 10]

print(subarr_maxsum(arr))



# def subarr_maxsum(arr):
#     max_sum=0
#     n=len(arr)
#     if len(arr) <= 1:
#         return arr[0] 
    
#     for i in range(n):
#         sum=0
#         for j in range(i,n):
#             sum = sum + arr[j]
        
#             if sum > max_sum:
#                 max_sum=sum
#     return max_sum
    
# # arr=[2, 3, 4, -1, 6, 10]
# # k=subarr_maxsum(arr)
# # print(k)

# def subarr_maxsum(arr):
#        n = len(arr)
#        maxSum = -1e8
#        currSum = 0
#        if n == 0:
#             return 0
#        if n == 1:
#            return arr[0]
           
#        for i in range(0, n):
#            currSum = currSum + arr[i]
#            if(currSum > maxSum):
#                maxSum = currSum
#            if(currSum < 0):
#                currSum = 0
      
#        return maxSum