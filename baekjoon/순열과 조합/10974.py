import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [x+1 for x in range(n)]

b = list(permutations(a))

for x in b:
    for y in x:
         print(y, end=" ")
    print()