N = int(input())

group_number = 0

for i in range(N):
  existing_words = []
  word = input()
  group_number += 1
  for j in range(1, len(word)):
    if word[j] in existing_words:
      group_number -= 1
      break
    if word[j] != word[j-1]:
      existing_words.append(word[j-1])

print(group_number)

