A = int(input())
B = int(input())
C = int(input())

result = A * B * C

result = str(result)

count = [0 for _ in range(10)]

for i in result:
  count[int(i)] += 1

for c in count:
  print(c)