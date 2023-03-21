A = [1, 2, 1, 1]
B= [1, 2]

def freq_query(A,B):
    A_dict={}
    for i in A:
        if i in A_dict:
            A_dict[i]+=1
        else:
            A_dict[i]=1
        
    freq_list=[]
    for i in B:
        freq_list.append(A_dict.get(i,0))
    return freq_list

print(freq_query(A,B))