nums=[0,0,1,1,1,2,2,3,3,4]
ans=[]
count = 0
# Loop for all the elements in the array
for i in range(len(nums)):
    # If the current element is equal to the next element, we skip
    if i < len(nums) - 2 and nums[i] == nums[i + 1]:
        ans.append(nums[i])
        continue
        
    # We will update the array in place
    nums[count] = nums[i]
    print(nums[count], "=" ,nums[i])
    count += 1
    print("count=",count)
print(count)
print(ans)