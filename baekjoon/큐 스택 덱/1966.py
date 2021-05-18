import queue

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    q = queue.Queue()
    for idx, x in enumerate(a):
        q.put([idx, x])

    a.sort()
    
    cnt = 0
    while not q.empty():
        idx, val = q.get()
        # 우선순위가 최대이면 pop, 아니면 큐 맨 뒤에 넣기
        if val == a[-1]:
            a.pop()
            cnt += 1
            if idx == m:
                break
        else:
            q.put([idx, val])
    print(cnt)

