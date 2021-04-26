import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def calculate_score(people):
    if len(people) == 1:
        return 0
    score = 0
    temp = list(combinations(people, 2))
    for t in temp:
        i, j = t
        score += a[i-1][j-1] + a[j-1][i-1]
    return score

people = set(range(1, n+1))
ans = 1e9
for i in range(2, n):
    comb = list(combinations(range(1, n+1), i))
    for c in comb:
        start = set(c)
        link = people - start
        start_score = calculate_score(start)
        link_score = calculate_score(link)
        diff = abs(start_score - link_score)
        ans = min(ans, diff)

print(ans)


    