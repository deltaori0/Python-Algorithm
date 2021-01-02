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