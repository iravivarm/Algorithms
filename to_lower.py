A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']


for i in range(len(A)):
    if (ord(A[i])>=65 and ord(A[i])<= 90):
        A[i]=chr(ord(A[i])+32)
print(A)


















# def to_lower(A):
#     arr=[]
#     for char in range(0, len(A)):
#         if (A[ord(char)] >= ord('A')) and (A[ord(char)] <= ord('Z')):
#             A[char]=chr(ord(char)+32)
#             print(A[char])

#             # A[ord(char)]=chr(ord(char)+32)
#     return A
#     # else:
#     #     print(chr(ord(char)+32))

# print(to_lower(A))
