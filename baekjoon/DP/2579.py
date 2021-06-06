import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stair = [int(input()) for _ in range(n)]

# dp[n] = 계단 i까지 오를 때의 최댓값
# dp[n] = max(직전 칸에서 올라온 경우 최댓값, 전전 칸에서 올라온 경우의 최댓값)
# dp[n] = max(stair[n]+stair[n-1]+dp[n-3], stair[n]+dp[n-2])
# stair = [10, 20, 15, 25, 10, 20]

dp = []
dp.append(stair[0])
if n >= 2:
    dp.append(max(stair[1]+stair[0], stair[1]))
if n >= 3:
    dp.append(max(stair[2]+stair[1], stair[2]+stair[0]))

for i in range(3, n):
    dp.append(max(stair[i]+stair[i-1]+dp[i-3], stair[i]+dp[i-2]))

ans = dp.pop()
print(ans)