n = int(input())
a = list(map(int, input().split()))

cnt = 0

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for x in a:
    if is_prime(x):
        cnt += 1

print(cnt)