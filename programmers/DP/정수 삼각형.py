def sum_path(triangle, i, j):
    if i >= len(triangle):
        return 0
    cur = triangle[i][j]
    sum_left = cur + sum_path(triangle, i+1, j)
    sum_right = cur + sum_path(triangle, i+1, j+1)
    print(max(sum_left, sum_right))
    return max(sum_left, sum_right)

def solution(triangle):
    answer = 0
    answer = sum_path(triangle, 0, 0)
    return answer