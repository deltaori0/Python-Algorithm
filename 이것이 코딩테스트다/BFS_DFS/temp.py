def solution(prices):
    answer = []
    while prices:
        cur = prices.pop(0)
        cnt = 0
        for p in prices:
            cnt += 1
            if cur > p:
                break
        answer.append(cnt)
    return answer

def find_same_name(lst):
    a = lst
    b = list(set(lst))
    for i in b:
        a.remove(i)
    return a[0]

def solution(participant, completion):
    answer = ''
    p = set(participant)
    c = set(completion)
    
    result = p - c
    if not result:
        answer = find_same_name(participant)
    else:
        answer = ''.join(result)
        
    return answer

import itertools
from collections import Counter # 리스트에 있는 요소 개수 셀 때 사용

def solution(clothes):
    # 모든 조합을 다 만들어 놓고 거기서 같은 종류인 것인 경우를 뺀다
    # 1. 모든 조합 만들기
    # itertools의 combinations 사용
    # 2. 같은 종류 빼기
    # 전체 조합 리스트를 반복문을 통해 돌아가며 [1]의 요소가 중복된 것이 있는지 확인
    
    combinations = []
    for i in range(1, len(clothes)+1):
        temp = []
        temp = list(itertools.combinations(clothes, i))
        combinations.extend(temp)
    
    cnt = len(combinations)
    print(combinations)
    for c in combinations:
        for i, lst in enumerate(c):
            l = list(c[i+1:])
            if l:
                print(l[0])
                if lst[1] in l[0]:
                    cnt -= 1
    return cnt


    for key, val in dic.items():
        print(key, val)
        temp.append(val)
    print(Counter(temp))



def solution(s):
    answer = 0
    # 1. 문자열 자르기 (1, 2, 3, ... , 문자열 길이만큼)
    # 2. 자른 문자열들의 길이를 length 배열에 넣기
    # 3. min을 사용해서 가장 짧은 길이를 리턴하기
    # 주의할 점 : 2번에서 길이가 1인 문자열은 +1을 하지 않고 나머지는 +1
    
    length = []
    # 문자열 자르기
    for i in range(1, len(s)+1):
        temp = []
        for j in range(0, len(s), i):
            temp.append(s[j:j+i]) 
        # 문자열 길이 구하기
        cur = ''
        seq = 0
        l = 0
        for t in temp:
            if cur == t:
                if seq == 0:
                    l -= i
                    l += i + 1
                if seq >= 10:
                    l += 1
                elif seq >= 100:
                    l += 2
                elif seq >= 1000:
                    l += 3
                seq += 1
                continue
            cur = t
            seq = 0
            l += len(t)
        length.append(l)
    
    answer = min(length)
            
    return answer