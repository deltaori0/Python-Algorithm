import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = []
num = 1

flag = True
ans = []
for _ in range(n):
    x = int(input())
    while num <= x:
        s.append(num)
        ans.append('+')
        num += 1
    
    if x == s[-1]:
        s.pop()
        ans.append('-')
    else:
        flag = False

if flag:
    print('\n'.join(ans))
else:
    print('NO')

