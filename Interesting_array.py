A=[9,17]

xor_val=0
for num in A:
    xor_val  = xor_val ^ num
if xor_val & 1 == 0:
    print("yes")
else:
    print("no")
