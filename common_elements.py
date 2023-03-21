def solve(self, A, B):
    dict_a = {}
    result = []
    for a in A:
        if dict_a.__contains__(a):
            dict_a[a] += 1
        else:
            dict_a[a] = 1
    for b in B:
        if dict_a.__contains__(b) and dict_a[b] != 0:
            result.append(b)
            dict_a[b] -= 1
    return result
