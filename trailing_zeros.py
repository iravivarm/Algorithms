
if A == 0:
    print("1")
factorial=1
for i in range(1, A+1):
    factorial = factorial * i
print(factorial)

trailing_zero_count=0
while factorial > 0:
    print(factorial)
    if (factorial % 10) == 0:
        trailing_zero_count += 1
        factorial=factorial // 10 
    else:
        break

print(trailing_zero_count)