from itertools import combinations

n, m = map(int, input().split())
ice = list(combinations(range(1, n+1), 3))

# n x n의 2차원 배열 -> 맛 없는 아이스크림 조합 체크
no_mat = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    no_mat[x][y] = 1
    no_mat[y][x] = 1

ans = 0
for x in ice:
    # 하나라도 체크되어 있으면
    if no_mat[x[0]][x[1]] or no_mat[x[0]][x[2]] or no_mat[x[1]][x[2]]:
        continue
    ans += 1

print(ans)