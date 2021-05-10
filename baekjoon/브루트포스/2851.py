a = [int(input()) for _ in range(10)]

min_diff = 100
sum = 0
for i in range(len(a)):
    temp = sum + a[i]
    if abs(100 - temp) <= min_diff:
        sum += a[i]
        min_diff = abs(100 - sum)
    else:
        break


print(sum)