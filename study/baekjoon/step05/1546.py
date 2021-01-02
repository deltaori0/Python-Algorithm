N = int(input())
scores = list(map(int, input().split()))
scores.sort()

M = scores[N-1]
new_scores = []

for s in scores:
  new_score = s / M * 100
  new_scores.append(new_score) 

total = sum(new_scores)
avg = total / N

print(avg)