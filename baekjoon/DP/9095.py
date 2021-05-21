# 4를 만드려면 : ((3을 만드는 방법) + 1), ((2를 만드는 방법) + 2), ((1을 만드는 방법) + 3)
# 따라서 개수는 그냥 f(n-1) + f(n-2) + f(n-3) 해주면 됨

t = int(input())

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return f(n-1) + f(n-2) + f(n-3)
    

for _ in range(t):
    n = int(input())
    print(f(n))