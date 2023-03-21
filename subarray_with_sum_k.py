
nums = [2,3,8,10,11,0,10,1]
k=11
ans=0
prefsum=0
d={}
print(d)

for num in nums:
    prefsum = prefsum + num
    print("prefix_sum:",prefsum)

    if prefsum-k in d:
        print("prefsum-k:",prefsum-k)
        ans = ans + d[prefsum-k]
        print("if_ans", ans)

    if prefsum not in d:
        d[prefsum] = 1
        print("elif_d:",d)
    else:
        d[prefsum] = d[prefsum]+1
        print("else_d:",d)
print("ans:",ans)