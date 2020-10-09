import sys

T = int(input())
for i in range(T):
  result = []
  R, S = sys.stdin.readline().split()
  for s in S:
    result.append(s*int(R))
  for r in result:
    print(r, end="")
  print()

