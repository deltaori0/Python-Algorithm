while True:
    w, h = map(int, input().split())
    maps = []
    
    if w == 0 and h == 0:
        break
    
    for _ in range(h):
        tmp = list(map(int, input().split()))
        maps.append(tmp) # 리스트 자체가 저장되어서 2차원 리스트가 된다

    print(maps)

