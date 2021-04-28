import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]
# n 번째 날의 수익 = max (n+1 번째 날의 수익, n 번째 수익 + Tn 지난 후 수익)
# 뒤에서부터 계산
for i in range(n-1, -1, -1):
    if i + a[i][0] > n: # 날짜 넘어가는 경우
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], a[i][1] + dp[i + a[i][0]])

print(dp[0])