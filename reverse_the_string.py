A = "crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv "
def reverse_words(A):
    print(A)
    a=A.split(" ")[::-1]
    print(a)
    rev_list=[]

    for i in a:
        rev_list.append(i)
    rev_string=" ".join(rev_list)
    return rev_string.strip()


print(reverse_words(A))