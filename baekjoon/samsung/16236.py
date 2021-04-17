import sys

n = int(input())
area = []

# [row_idx, column_idx]
shark_pos = []

# 공간 initialize
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    # 아기 상어 위치 찾기
    if 9 in temp:
        shark_pos = [i, temp.index(9)]
    area.append(temp)

# print("area", area)
# print("shark", shark_pos)

while True:
    for row in area:
        