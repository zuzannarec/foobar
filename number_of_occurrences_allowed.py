

def solution(data=[1,2,2,3,3,3,4,5,5], n=1):
    if n < 1:
        return list()
    count = dict()
    for num in data:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    i = 0
    j = 0
    while i < len(data):
        while j < len(data) and count[data[j]] > n:
            j += 1
        if j >= len(data):
            return data[:i]
        data[i] = data[j]
        i += 1
        j += 1
    return data[:i]


solution()