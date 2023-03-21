A="ABCGAGG"

def sub_sequnce(A):
    count=0
    pair=0
    for i in A[::-1]:
        
        if i == "G":
            count = count+1
        
        if i == "A":
            pair = pair + count
    return pair    
