import itertools

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    # numbers 문자열을 각각의 문자로 분리
    # permutation
    # int로 바꾸기 (맨 앞에 0인 애들은 자동으로 똑같이 되겠지?)
    # set을 이용해서 고유 숫자 뽑아내기
    # 소수 찾기 함수
    
    perm = []
    for i in range(1, len(numbers)+1):
        temp = list(map(''.join, itertools.permutations(numbers, i)))
        perm.extend(temp)
    
    result = set(list(map(int, perm)))
    
    count = 0
    for n in result:
        if is_prime(n):
            count += 1
            
    return count