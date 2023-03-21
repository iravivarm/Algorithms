A=[1,-1,-2,2]
pf=[0]*len(A)
print("pf", pf)
pf_sum=0

A_dict={}
count=0
n=len(A)

for i in range(n):
    pf[i]=pf[i-1]+A[i]



for i in range(n):
    if pf[i]==0:
        count=count + 1
    if pf[i] in A_dict:
        count =count + A_dict[pf[i]]
        print("count=",count + A_dict[pf[i]])
        A_dict[pf[i]] += 1
        print("A_dict=",A_dict)
    else:
        A_dict[pf[i]] = 1
print(count)

        

