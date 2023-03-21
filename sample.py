print(end="Enter the String: ")
text = input()
textLen = len(text)
nums = []
chk = 0
for i in range(textLen):
  if text[i].isdigit():
    nums.append(text[i])
    chk = 1
    
if chk==1:
  print("\nHere are the list of Numbers in String: ")
  numsLen = len(nums)
  for i in range(numsLen):
    print(end=nums[i] + " ")
else:
  print("\nNumber is not available in the list!")