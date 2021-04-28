days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

x, y = map(int, input().split())

total = 0
for i in range(x-1):
    total += days[i]

ans = day[(total-1+y) % 7]

print(ans)