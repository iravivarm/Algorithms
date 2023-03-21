def solve(A):
    printNum(A)
    print("")
def printNum(A):
    if A==1:
        print(1, end=" ")
        return
    printNum(A-1)
    print(A,end=" ")

solve(10)