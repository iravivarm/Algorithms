A = [1,2,3]
B=12
A=len(C)

max_sum=0
for i in range(A):
    sum=0
    for j in range(i,A):
        sum = sum+C[j]
        
        if sum > max_sum and sum <=B:
            max_sum=sum

print(max_sum)


############################################Sunarray total_sum#############
def subarraySum(self, A):
    max_sum=0
    n = len(A)
    for i in range(len(A)):
        max_sum=max_sum + A[i] * (i+1) * (n-i)
    return max_sum



