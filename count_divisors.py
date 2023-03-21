import math
A=[2,3,4,5]


#spf=[0, 1, 2, 3]

#print(spf)
def spf_A(n):
    spf=[i for i in range(n)]
    i=2
    num_range=math.sqrt(len(spf))
    print(num_range)

    while i <= num_range:
        print("i",i)
        if spf[i] == i:
            j=i*i
            print("j:",j)
            while j < n:
                if spf[j] == j:
                    spf[j] = i
                j = j +i
        i = i+1
    return spf

def primefactors(spf,n):
    total = 1
    while n > 1:
        prime = spf[n]
        count = 0
        while n % prime == 0:
            count += 1
            n = n // prime
            
        total = total * (count +1)
    return total

    
spf = spf_A(max(A)+1)
res = []
for k in range(len(A)):
    value = primefactors(spf,A[k])
    res.append(value)

# def createspf(n):
#     spf = [i for i in range(n)]
#     rng = math.sqrt(len(spf))
#     i = 2
#     while i < rng:
#         if spf[i] == i:
#             j = i * i
#             while j < n:
#                 if spf[j] == j:
#                     spf[j] = i
#                 j += i
#         i += 1
#     return spf

spf = spf_A(max(A)+1)
print(spf)
