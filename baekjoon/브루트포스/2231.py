n = int(input())

for i in range(1, n+1):
    num = list(map(int, str(i)))
    bunhaehop = i + sum(num)
    if bunhaehop == n:
        print(i)
        break
else:
    print(0)