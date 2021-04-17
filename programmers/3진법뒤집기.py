def solution(n):
  answer = 0
  ternary = []
  while True:
    if n // 3 == 0:
      ternary.append(n)
      break
    ternary.append(n % 3)
    n = n // 3
  
  ternary.reverse()
  for i in range(len(ternary)):
    answer += pow(3, i) * ternary[i]

  return answer

print(solution(125))