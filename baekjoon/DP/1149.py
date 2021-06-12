import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n)]
dp[0] = a[0]
# N 번째에 칠할 수 있는 경우
# f(n, R) = min(f(n-1, G), f(n-1, B)) + price(n, R)
# f(n, G) = min(f(n-1, R), f(n-1, B)) + price(n, G)
# f(n, B) = min(f(n-1, R), f(n-1, G)) + price(n, B)

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + a[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + a[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + a[i][2]

print(min(dp[-1]))

