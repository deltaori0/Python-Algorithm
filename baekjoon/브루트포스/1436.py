n = int(input())

cnt = 0

num = 1

while True:
    if cnt == n:
        print(num-1)
        break
    if str(num).find('666') != -1:
        cnt += 1
    num += 1

