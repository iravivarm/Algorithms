A=[4,1,2,3]
def count_sort(A,n):
    a_dict=dict()
    n=len(A)
    for i  in range(len(A)):
        a_dict[i]=0
    print(a_dict)
    for i in A:
        if i in a_dict:
            a_dict[i] += 1
        else:
            a_dict[i]=1

    print(a_dict)

    sorted_array=[]
    i=0
    while len(A) > 0:
        if a_dict[i] == 0:
            i +=1

        else:
            sorted_array.append(i)
            a_dict[i]-=1
            n=n-1
    return sorted_array


def printArr(A, n):
	print("Sorted Array: ");
	for i in range(0,n):
		print(vec[i], " ");