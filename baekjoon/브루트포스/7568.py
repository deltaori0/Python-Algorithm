n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(len(a)):
    s = 0
    height, weight = a[i][0], a[i][1]
    for j in range(len(a)):
        if i == j: continue
        if height < a[j][0] and weight < a[j][1]:
            s += 1
    print(s+1, end=" ")
    