a = input().split()
A = int(a[0])
B = int(a[1])
C = int(a[2])

print((A+B) % C)
print(((A%C) + (B%C))%C)
print((A*B) % C)
print(((A%C) * (B%C))%C)