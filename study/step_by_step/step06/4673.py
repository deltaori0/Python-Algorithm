def d(n):
  num = n
  temp = str(n)
  result = n

  for i in range(len(temp)):
    result += int(temp[i])

  return result

self_numbers = set(range(1, 10001))
temp = set()

for i in range(1, 10001):
  new_num = d(i)
  while True:
    if new_num > 10000:
      break
    temp.add(new_num)
    new_num = d(new_num)

result = list(self_numbers - temp)
result.sort()

for r in result:
  print(r)