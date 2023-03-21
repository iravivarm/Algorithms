def solve(A):
    n=len(A)
    return is_pallindrome(A, 0, n-1)

def is_pallindrome(A, left, right):
    if left > right: 
        return 1
    if A[left] != A[right]: 
        return 0
    return is_pallindrome(A, left+1, right-1)



print(solve("nama"))
