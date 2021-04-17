# 카펫 - yellow, brown

def check_brown(brown, a, b):
    if 2 * (a + b) + 4 == brown:
        return True
    else:
        return False

def solution(brown, yellow):
    answer = []
    # yellow의 약수를 구한다
    # 약수 중에서 brown 만족하는 조합 구한다
    
    for i in range(1, yellow+1):
        q, r = divmod(yellow, i)
        if r == 0:
            if q > yellow // q:
                width, height = q, yellow // q
            else:
                width, height = yellow // q, q
    
            if check_brown(brown, width, height):
                answer.extend([width + 2, height + 2])
                break
    return answer