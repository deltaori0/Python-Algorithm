# 효율성 개선 필요
from itertools import product

def solution(n):
    answer = ''
    
    nums = [1, 2, 4]
    lst = []
    for x in range(1, n+1):
        if len(lst) >= n:
            break
        lst += list(product(nums, repeat=x))
    answer = lst[n-1]
    
    answer = ''.join(map(str, answer))
    
    return answer