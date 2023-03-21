A = [ [1,1,2,5,6],
      [1,1,4,6,8],
      [2,6,7,9,-10] ]
print(A)
print(len(A[0]))
n=len(A)
print(n)

pf_sum=0
for i in range(n):
    # print(A[i])
    for j in range(n):
        # print("A[i][j]:",A[i][j])
        # print("i:",i+1)
        # print("j:",j+1)
        # print("n-1:",n-i)
        # print("n-j:",n-j)
        pf_sum=pf_sum+A[i][j]*(i+1)*(j+1)*(n-i)*(n-j)

print(pf_sum)
