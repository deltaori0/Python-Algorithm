A, B = input().split()
reversed_a = list(reversed(A))
reversed_b = list(reversed(B))

a = int(''.join(reversed_a))
b = int(''.join(reversed_b))

if a > b:
  print(a)
else:
  print(b)
