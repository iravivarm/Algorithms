A=4
B=5


def kth_value(A,B):
    if A == 0:
        return 0
    if B%2==0:
        return kth_value(A-1,B//2)
    return kth_value(A-1,B//2)

print(kth_value(A,B))


#      0
#     0 1
#   0 1 1 0
#  0 1 1 0 1 0 0 1 