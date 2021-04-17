def BFS(start_node):
    # 1) queue에 첫 번째 노드 넣으면서 시작
    queue = [start_node, ]

    while True:
        # 2) queue가 비어있는지 확인
        if len(queue) == 0:
            print('All node searched.')
            return None
        
        # 3) queue에서 맨 앞의 노드를 dequeue (0번 인덱스를 pop)
        node = queue.pop(0)

        # 4 만약 node가 찾고자 하는 target이면 서치 중단!
        if node == TARGET:
            print('The target found.')
            return node
        
        # 5) node의 자식을 expand해서 children에 저장
        children = expand(node)

        # 6) children을 stack에 쌓기
        queue.extend(children)