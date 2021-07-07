from itertools import permutations

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    e = [list(map(int, input().split())) for _ in range(n)]
    perm = list(permutations(range(1, n)))
    
    min_sum = 99999999
    for p in perm:
        sum = 0
        temp = [0] + list(p) + [0]
        for t in range(len(temp)-1):
            sum += e[temp[t]][temp[t+1]]

        if sum < min_sum:
            min_sum = sum


    print("#{} {}".format(test_case, min_sum))
