a = map(int, input().split())

total = 0
for x in a:
    total += x**2

print(total % 10)