n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

cnt = {}
for x in a:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1

for x in b:
    if x in cnt:
        print(cnt[x], end=" ")
    else:
        print(0, end=" ")