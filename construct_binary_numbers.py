A=3
B=2
def binary_numbers(A,B):
    tem=""
    dec=0
    rem=0
    power=0
    for i in range(A):
        tem = tem + "1"

    for i in range(B):
        tem = tem + "0"
    temp=int(tem)
    while temp:
        rem=temp%10
        dec=dec+rem*(2**power)
        power+=1
        temp //= 10

    return dec


print(binary_numbers(A,B))
