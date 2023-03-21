A = [ 96, -71, 18, 66, -39, -32, -16, -83, -11, -92, 55, 66, 93, 5, 50, -45, 66, -28, 69, -4, -34, -87, -32, 7, -53, 33, -12, -94, -80, -71, 48, -93, 62 ]

def subarray_with_sum_0(A):
    A_set=set()
    pf_sum=0
    for i in A:
        pf_sum=pf_sum + i
        if pf_sum==0 or pf_sum in A_set:
            return 1
        A_set.add(pf_sum)
    return 0

print(subarray_with_sum_0(A))