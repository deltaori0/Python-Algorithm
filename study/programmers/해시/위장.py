from collections import Counter

def solution(clothes):
    dic = dict(clothes)
    temp = []

    for val in dic.values():
        temp.append(val)

    count = dict(Counter(temp))

    result = 1
    for val in count.values():
        result *= (val+1)

    return result-1