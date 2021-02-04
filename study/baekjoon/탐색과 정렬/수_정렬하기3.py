# 메모리 제한
import sys
n = int(sys.stdin.readline())
numbers = [0 for _ in range(10001)] # 0 ~ 10000까지 index에 0 넣기
for _ in range(n):
   numbers[int(sys.stdin.readline())] += 1

for i, n in enumerate(numbers):
    if n > 0:
        for _ in range(n):
            print(i)