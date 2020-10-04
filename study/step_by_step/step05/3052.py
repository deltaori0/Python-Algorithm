num_list = []
for i in range(10):
  n = int(input())
  num_list.append(n)

diff = 0
remainder = []

for n in num_list:
  if n % 42 in remainder:
    continue
  remainder.append(n%42)
  diff += 1

print(diff)