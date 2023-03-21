
def is_pallindrome(num):
    temp = num
    reverse = 0
    while num > 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num = num // 10
    
        if reverse == temp:
           print("Hey, Its a Palindrome Number")
        


k = is_pallindrome(91019)


