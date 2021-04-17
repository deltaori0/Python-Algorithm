import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = []
for _ in range(n):
    name, kor, eng, mat = input().split()
    a.append([name, int(kor), int(eng), int(mat)])

a.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for x in a:
    print(x[0])