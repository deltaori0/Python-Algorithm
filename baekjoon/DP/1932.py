n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 맨 위에서부터 아래로 내려오면서 최대 값을 저장
max_path = [[] for _ in range(n)]
max_path[0].append(a[0][0])

for i in range(1, n):
    for j in range(len(a[i])):
        if j == 0:
            max_path[i].append(a[i][j] + max_path[i-1][j])
        elif j == len(a[i]) - 1:
            max_path[i].append(a[i][j] + max_path[i-1][j-1])
        else:
            max_path[i].append(max(a[i][j] + max_path[i-1][j-1], a[i][j] + max_path[i-1][j]))

print(max(max_path[-1]))