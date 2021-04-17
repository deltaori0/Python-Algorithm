S = input()
alphabet_list = [-1 for _ in range(26)]

for i in range(len(S)):
  index = ord(S[i]) - ord("a")
  if alphabet_list[index] != -1:
    continue
  alphabet_list[index] = i

for a in alphabet_list:
  print(a, end=" ")