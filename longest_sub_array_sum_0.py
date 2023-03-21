A=[ 9, -20, -11, -8, -4, 2, -12, 14, 1 ]
def longest_subarray_with_sum_0(A):
    ans=0
    pf_sum=0
    arr_dict={}
    for num in range(len(A)):
        pf_sum=pf_sum + A[num]
        if pf_sum == 0:
            ans=max(ans,num+1)
        elif pf_sum in arr_dict:
            ans=max(ans, num-arr_dict[pf_sum])
        else:
            arr_dict[pf_sum]=num
    return ans

print(longest_subarray_with_sum_0(A))
