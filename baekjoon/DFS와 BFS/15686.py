from itertools import combinations as cb

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 치킨집들의 좌표 리스트와 집들의 좌표 리스트를 만들어 주기
# chicken = list()
# home = list()
# for i in range(n):
#     for j in range(n):
#         if a[i][j] == 2:
#             chicken.append([i, j])
#         elif a[i][j] == 1:
#             home.append([i, j])

# 코드 짧은 방식
chicken = [[i, j] for i in range(n) for j in range(n) if a[i][j] == 2]
home = [[i, j] for i in range(n) for j in range(n) if a[i][j] == 1] 

# 치킨집 위치 중에서 m개를 뽑기
chi_list = list(cb(chicken, m))

# 특정 집과 여러 치킨집 중 가장 짧은 거리 계산
def calc_dist(ho, chi_list):
    min_dist = 1e9  # 1 * 10^9
    for chi in chi_list:
        dist = abs(chi[0] - ho[0]) + abs(chi[1] - ho[1])
        min_dist = min(min_dist, dist)
    return min_dist

ans = []
for chi in chi_list:
    total = 0
    for h in home:
        total += calc_dist(h, chi)
    ans.append(total)

print(min(ans))