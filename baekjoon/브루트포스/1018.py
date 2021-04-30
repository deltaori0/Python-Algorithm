import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = [input() for _ in range(n)]

ans = []
for x in range(n-7):
    for y in range(m-7):
        count1 = 0  # W로 시작
        count2 = 0  # B로 시작
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j) % 2 == 0:
                    if a[i][j] != 'W': count1 += 1
                    if a[i][j] != 'B': count2 += 1
                else:
                    if a[i][j] != 'B': count1 += 1
                    if a[i][j] != 'W': count2 += 1
        if count1 < count2:
            ans.append(count1)
        else:
            ans.append(count2)

print(min(ans))
        