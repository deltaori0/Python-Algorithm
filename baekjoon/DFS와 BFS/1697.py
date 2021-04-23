import queue
n, k = map(int, input().split())

q = queue.Queue()
a = [0] * 100001
a[n] = 1
q.put(n)

def get_next(x):
    return [x-1, x+1, x*2]

while not q.empty():
    x = q.get()
    if x == k:
        print(a[x]-1)
        break

    moves = get_next(x)
    for i in range(3):
        nx = moves[i]

        if nx < 0 or nx > 100000: continue # 범위 벗어난 경우
        if a[nx] != 0: continue # 이미 한 번 방문한 경우

        a[nx] = a[x] + 1
        q.put(nx)