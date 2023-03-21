def reverse_num(num):
    rev = 0 
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num//10
        
    return rev


kn = reverse_num(23456987)
print(kn)



