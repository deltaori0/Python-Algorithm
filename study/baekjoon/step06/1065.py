def is_hansu(x):
  input_num = str(x)
  length = len(input_num)
  if length == 1:
    return True
  difference = int(input_num[1]) - int(input_num[0])
  for i in range (length-1):
    if int(input_num[i+1]) - int(input_num[i]) != difference:
      return False
  return True

N = int(input())
count = 0
for i in range(1, N+1):
  if is_hansu(i) == True:
    count += 1

print(count)