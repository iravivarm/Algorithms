A=[1, 1, 2, 2]
B=2

def distinct_num_window(A,B):
    ans=[]
    n=len(A)
    freq_dict={}

    if B>n:
        return ans

    for i in range(B):
        if A[i] in freq_dict:
            freq_dict[A[i]] += 1
        else:
            freq_dict[A[i]] = 1
    ans.append(len(freq_dict))
    
    # adding Incoming_element and removing outgoing element
    for i in range(B,n):
        if A[i] in freq_dict:
            freq_dict[A[i]] += 1
        else: 
            freq_dict[A[i]] = 1
        freq_dict[A[i-B]]-=1
        if freq_dict[A[i-B]] == 0:
            del freq_dict[A[i-B]]
        ans.append(len(freq_dict))
    return ans

print(distinct_num_window(A,B))


