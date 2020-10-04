N = int(input())

a = N // 10
b = N % 10
c = a + b

cycle = 1

while True: 
  new_num = b * 10 +  c % 10
  if new_num == int(N):
    break
  a = new_num // 10
  b = new_num % 10
  c = a + b
  cycle += 1

print(cycle)