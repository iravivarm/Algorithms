A = [3,5, 1, 2]
B = 8

cnt=0
n=len(A)
hm={}

for i in range(len(A)):
    target=B-A[i]
    if target in hm:
        cnt=cnt+hm[target]
    if A[i] in hm:
        hm[A[i]]+=1
        print("exists:",A[i])
    else:
        hm[A[i]]=1
        print("not_exists:",A[i])

print(cnt,hm)