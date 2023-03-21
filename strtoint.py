def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    s=s.strip()
    is_Negative=False
    is_Positive=False
    is_Decimal=False
    final_value=0
    decimal_count=0
    i=0 

    if len(s)>1 and s[0] == "-":
        is_Negative=True
    if len(s)>1 and s[0] == "+":
        is_Positive=True

    if is_Negative:
        i +=1
    if is_Positive:
        i +=1

    while i < len(s) and "0" <= s[i] <= "9":
        if s[i] not in [".",","]:
            final_value=final_value * 10 + (ord(s[i])-ord("0"))
        if s[i] == ".":
            is_Decimal=True
            decimal_count=1
        if is_Decimal:
            decimal_count+=1

        i = i+1

    if is_Decimal:
        final_value=final_value*(0.1**decimal_count)

    if is_Negative:
        final_value= final_value*-1
    
    if final_value < -2**31:
        return (-2**31)
    if final_value > 2**31 - 1:
        return (2**31-1)
    return final_value