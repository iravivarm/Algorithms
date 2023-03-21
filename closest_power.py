def pow2(num):
    x = 0
    while 2**(x+1) < num:
        x += 1
    return 2**x

print(pow2(18))