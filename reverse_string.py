a="scaleracademy"



def rev_string(A):
    n=len(a)
    if n<=0:
        return ""
    return A[n-1]+rev_string(A[:-1])

def main():
    string=input()
    s=rev_string(string)
    print(s)

if __name__ == '__main__':
    main()