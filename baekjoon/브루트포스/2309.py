from itertools import combinations
a = [int(input()) for _ in range(9)]

comb = list(combinations(a, 7))
ans = []
for c in comb:
    if sum(c) == 100:
       ans.extend(list(c))
       break

ans.sort()
for x in ans:
    print(x)