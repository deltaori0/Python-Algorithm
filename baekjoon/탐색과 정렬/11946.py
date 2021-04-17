import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, q = map(int, input().split())
a = []

for _ in range(q):
    time, team, num, result = input().split()
    a.append([int(time), int(team), int(num), result])


# team, score, total_time, 딕셔너리 - 문제 번호 별 시도 횟수, 푼 문제 목록
b = [[i+1, 0, 0, {x+1: 0 for x in range(m)}, []] for i in range(n)]

for time, team, num, result in a:
    idx = team-1
    if result == 'AC':
        # score
        if num in b[idx][4]:    # 이미 풀었던 문제면 스킵
            pass
        else:
            # score
            b[idx][1] += 1
            # total_time
            b[idx][2] += time + 20 * b[idx][3][num]
            # 푼 문제 목록에 추가
            b[idx][4].append(num)
    else:
        # 딕셔너리에 문제 번호와 시도 횟수 업데이트
        b[idx][3][num] += 1

b.sort(key=lambda x: (-x[1], x[2], x[0]))

for x in b:
    print(x[0], x[1], x[2])