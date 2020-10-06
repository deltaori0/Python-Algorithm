import sys
T = int(input())

for i in range(T):
  result = input()
  sum = 0
  score = 0
  for j in result:
    if j == "X":
      score = 0
      sum += score
    else :
      score += 1
      sum += score
  print(sum)


