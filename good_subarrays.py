A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65

count = 0
n=len(A)
for i in range(n):
    sum=0
    size=0
    for j in range(i,n):
        sum= sum +A[j]
        size=size+1

        if size%2==0 and sum < B:
            count = count + 1
        elif size%2!=0 and sum>B:
                count=count + 1

print(count)