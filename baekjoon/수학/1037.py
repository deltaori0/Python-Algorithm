num = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 1
if len(a) == 1:
  ans = a[0]**2
else:
  ans = a[0] * a[-1]
print(ans)