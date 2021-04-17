def DFS(start_node):
    # stack에 첫 번째 노드 넣으면서 시작
    stack = [start_node, ]

    while True:
        # 2) stack이 비어있는지 확인
        if len(stack) == 0:
            print('All node searched.')
            return None
        
        # 3) stack에서 맨 위의 노드를 pop
        node = stack.pop()

        # 4) 만약 node가 찾고자 하는 target이라면 서치 중단!
        if node == TARGET:
            print('The target found.')
            return node
        
        # 5) node의 자식을 expand 해서 children에 저장
        children = expand(node)

        # 6) children을 stack에 쌓기
        stack.extend(children)  # list 끝에 iterable의 모든 항목을 넣는다