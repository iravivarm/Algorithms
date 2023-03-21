def josephus_problem(A):
    pow=0
    while 2 ** (pow + 1) <= A:
        pow=pow+1
    pow=2**pow
    print(pow)
    rem_persons=(A-pow)*2+1

    return rem_persons
    

print(josephus_problem(8))