a = input().split()
H = int(a[0])
M = int(a[1])

if M >= 45:
  print(H, M-45)
else:
  if H == 0:
    H = 24
  print(H-1, M+15)