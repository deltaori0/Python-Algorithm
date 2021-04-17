import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [ input() for _ in range(n)]

def sum_digit(x):
    total = 0
    for i in x:
        if i.isdigit():
            total += int(i)
    return total

a.sort(key=lambda x: (len(x), sum_digit(x), x))

for x in a:
    print(x)