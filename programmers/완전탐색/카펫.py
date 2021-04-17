import math

def solution(brown, yellow):
    answer = []
    for n in range(1, int(math.sqrt(yellow)) + 1):
        h, w = n, yellow / n
        if 2 * h + 2 * w + 4 == brown:
            answer.extend([w+2, h+2])
            break

    return answer