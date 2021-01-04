n = int(input())

dp = [0 for _ in range(n+1)]
dp[1] = 0

for i in range(2, n+1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i//2] + 1, dp[i-1] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i-1] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)
    else:
        dp[i] = dp[i-1] + 1
print(dp[n])
    
# 점화식
# f(x) = min(f(x-1) + 1, f(x/2) + 1, f(x/3) + 1)
# 재귀함수(top-down)를 매번 호출하면 시간 복잡도가 굉장히 커지므로 반복문(bottom-up) 방법
# 다이나믹 프로그래밍 - 즉, 리스트를 만들어 값으르 매번 저장
# 연산을 사용하는 횟수의 최솟값을 출력하라 - 연산을 최고의 효율로 진행하라

