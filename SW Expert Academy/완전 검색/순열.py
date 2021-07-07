# 방법 1
# 재귀적 구현
def perm(arr, depth, n, k):
    # depth 0부터 시작하여 k라면 k개를 모두 뽑은 것이므로 print 후 return
    if (depth == k):
        print(arr)
        return
    for idx in range(depth, n):
        # 각 depth에 대해 남아 있는 것들 중에 모두 뽑아보고
        # 해당 경우에 대해 재귀적으로 perm 함수를 돌리고
        # 원상복구 하여 다시 경우의 수를 찾는다
        arr[idx], arr[depth] = arr[depth], arr[idx]
        perm(arr, depth+1, n, k)
        arr[idx], arr[depth] = arr[depth], arr[idx]

# 방법 2 (이게 더 이해하기 편함)
def permutation(arr, r):
    arr = sorted(arr)   # 출력을 예쁘게 만들기 위해서 (선택)
    used = [0 for _ in range(len(arr))] # i 번째 값을 썼는지 저장

    def generate(chosen, used):
        # chosen 변수는 순열의 원소를 저장하는 배열
        # 값을 하나씩 추가하다가 개수가 r이 되는 순간 하나의 순열이 만들어진 것이므로 출력하고 종료
        if len(chosen) == r:
            print(chosen)
            return
        
        # 모든 순열은 arr의 0번째부터 i-1번째 값으로 시작하기 때문에 다 만든다
        for i in range(len(arr)):
            if not used[i]:
                # chosen에 값 추가 후 used에 해당 변수를 사용했다고 체크한 후 generate 반복
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                # 하나가 만들어진 후에는 그 값을 uncheck
                used[i] = 0
                chosen.pop()
    generate([], used)

permutation('ABCD', 4)