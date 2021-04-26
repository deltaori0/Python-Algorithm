import sys
from itertools import combinations

# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
people = set(range(1, n+1))
comb = list(combinations(people, n//2))

min_difference = 9999999
comb = comb[:len(comb)//2]

for c in comb:
    score1 = 0
    score2 = 0

    start = set(c)
    link = people - start

    start_comb = list(combinations(start, 2))

    for i, j in start_comb:
        score1 += s[i-1][j-1] + s[j-1][i-1]

    link_comb = list(combinations(link, 2))
    for i, j in link_comb:
        score2 += s[i-1][j-1] + s[j-1][i-1]

    diff = abs(score1 - score2)
    if diff < min_difference:
        min_difference = diff

print(min_difference)