A = "tHiSiSaStRiNg" 

ans=''
for i in A:
    if i >= 65 and ord(i) <=90:
        con=ord(i)+32
        ans+=chr(con)
    else:
        con1=ord(i)-32
        ans=ans+chr(con1)
print(ans)