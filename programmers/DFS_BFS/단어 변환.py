import queue

def convertable(a, b, l):
    dif = 0
    for i in range(l):
        if dif > 1:
            break
        if a[i] != b[i]:
            dif += 1
    if dif == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    # begin word를 하나 더 추가해서 convert matrix 생성
    words.append(begin)
    
    # target index
    if target in words:
        target_idx = words.index(target)
    else:
        return 0
    
    n = len(words)
    l = len(begin)
    convert_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if convertable(words[i], words[j], l):
                convert_matrix[i][j] = 1
                convert_matrix[j][i] = 1
    
    q = queue.Queue()
    chk = [False] * n
    
    # begin word를 queue에 삽입
    chk[n-1] = True
    q.put([n-1, 0])
    
    while not q.empty():
        idx, cnt = q.get()
        
        # 종료 조건
        if idx == target_idx:
            return cnt
        
        for i, x in enumerate(convert_matrix[idx]):
            if x == 1 and chk[i] == False:
                chk[i] = True
                q.put([i, cnt+1])