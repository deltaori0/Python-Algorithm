n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()

for x in a:
    print(x, end=" ")