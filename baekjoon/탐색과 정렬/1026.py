n = int(input())
ans = 0

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

for i in range(len(a)):
    min_a = min(a)
    max_b = max(b)
    idx_a = a.index(min_a)
    idx_b = b.index(max_b)
    ans += max_b * min_a
    del a[idx_a]
    del b[idx_b]

print(ans)