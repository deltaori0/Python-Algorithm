a = input().split()

A = int(a[0])
B = int(a[1])

if A > B:
  print(">")
elif A < B:
  print("<")
else:
  print("==")