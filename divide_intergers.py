dividend=300
divisor=-2

# sign=0
# if (dividend < 0) ^ (divisor<0):
#     sign=-1
# else:
#     sign=1


# dividend = abs(dividend)
# divisor = abs(divisor)
# quotient=0
# while dividend >= divisor:
#     dividend=dividend - divisor
#     quotient += 1

# if sign==-1:
#     quotient= -quotient
# print(quotient) 



sign=0
if (dividend < 0) ^ (divisor<0):
    sign=-1
else:
    sign=1

dividend = abs(dividend)
divisor = abs(divisor)
quotient=0
temp=0
for i in range(31, -1,-1):
    if (temp + (divisor << i)) <= dividend:
        temp = temp + (divisor << i)
        quotient = quotient | 1 << i

if sign==-1:
    quotient= -quotient
print(quotient) 

