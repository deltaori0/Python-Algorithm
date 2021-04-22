from itertools import permutations

k = int(input())
a = input().split()

nums = [x for x in range(10)]
p = list(permutations(nums, k+1))

ans = []
for x in p:
    flag = True
    for i in range(k):
        if a[i] == '<':
            if x[i] >= x[i+1]:
                flag = False
                break
        elif a[i] == '>':
            if x[i] <= x[i+1]:
                flag = False
                break
    if flag:
        ans.append(x)

max = ans[-1]
min = ans[0]

for x in max:
    print(x, end='')
print()
for x in min:
    print(x, end='')