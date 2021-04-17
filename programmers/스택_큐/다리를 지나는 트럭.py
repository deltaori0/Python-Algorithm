from collections import deque

def solution(bridge_length, weight, truck_weights):  
    # 매 스텝마다 3가지 연산
    # 1. 다리를 다 건넌 트럭이 있는지 확인하고 있으면 pop하기
    # 2. 다리 위에 있는 트럭 모두 한 칸 왼쪽으로 옮겨주기
    # 3. 대기 트럭 중에 다리 위에 올라갈 수 있는 트럭이 있는지 확인하기
    
    # deque 사이즈를 bridge_length 만큼 만들기
    # 초기화는 0으로 해서
    # pop할 때 0보다 큰 값이 나오면 그것부터가 진짜 값
    # 매번 왼쪽으로 옮기는 연산은 매번 큐를 pop하는 연산이고
    # 만약에 새로운 트럭이 다리 위에 올라가지 못한다면 0을 append하면 된다
    # 그렇다면 종료 조건은?
    # complete 개수를 세어서 이게 처음 len(truck_weights)와 같아질 경우!
    
    bridge = deque([0 for _ in range(bridge_length)])  
    waiting = deque(truck_weights)
    
    complete = 0
    l = len(truck_weights)
    cur_weight = 0
    time = 0
    
    while True:
        if complete == l:
            break
        
        # 왼쪽으로 옮기는 연산
        temp = bridge.popleft()
        if temp > 0:
            complete += 1
            cur_weight -= temp
        
        # 대기하는 트럭 확인
        if waiting:
            if cur_weight + waiting[0] <= weight:
                w = waiting.popleft()
                bridge.append(w)
                cur_weight += w
            else:
                bridge.append(0)
        else:
            bridge.append(0)
        
        time += 1
        
    return time