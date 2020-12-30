N = int(input())

min_list = []
q = N // 5
while q > -1:
    r = N - 5 * q
    if r % 3 == 0:
        min_list.append(q + r // 3)
    q -= 1

if min_list == []:
    answer = -1
else:
    min_list.sort()
    answer = min_list[0]

print(answer)