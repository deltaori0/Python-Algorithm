T = int(input())

dx = [0, 1]
dy = [1, 0]

def f(x, y, total):
    global min_result
    total += a[x][y]
    if x == n-1 and y == n-1:
        if total < min_result:
            min_result = total
        return total
    if total > min_result:
        return


    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n: continue
        if ny < 0 or ny >= n: continue
        f(nx, ny, total)

for t in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    min_result = 99999999
    f(0, 0, 0)
    print("#{} {}".format(t, min_result))

        

    
