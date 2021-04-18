import sys
from itertools import permutations as pm
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

p = list(pm(a))

max = 0
for x in p:
    sum = 0
    for i in range(n-1):
        sum += abs(x[i] - x[i+1])
    if sum > max:
        max = sum

print(max)