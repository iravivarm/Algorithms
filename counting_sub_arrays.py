A = [1, 11, 2, 3, 15]
B = 10

count=0
n=len(A)
for i in range(n):
    sum=0
    for j in range(i,n):
        sum = sum + A[j]

        if sum <= B:
            count = count + 1
print(count)