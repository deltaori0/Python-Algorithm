def combination(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen):
        # chosen에 저장된 아이템 개수가 r개이면 조합이 하나 완성된 것 -> 출력 후 종료
        if len(chosen) == r:
            print(chosen)
            return
        
        # start는 chosen이 비어있을 때는 0
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        # chosen에 저장된 마지막 값 다음을 넣는다
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                generate(chosen)
                chosen.pop()
    
    generate([])

combination('ABCDE', 2)