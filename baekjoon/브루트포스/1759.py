import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
vowels = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
a = input().split()
a.sort()

comb = list(combinations(a, l))

for c in comb:
    count = 0
    for x in c:
        if x in vowels:
            count += 1
    
    if 1 <= count <= l-2:
        print(''.join(c))