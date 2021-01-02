word = input()
alphabet_list = [0 for _ in range(26)]

for w in word:
  index = ord(w.upper()) - ord("A")
  alphabet_list[index] += 1

max = -1
max_index = -1
max_count = 0
for i in range(len(alphabet_list)):
  if alphabet_list[i] == max:
    max_count += 1
  elif alphabet_list[i] > max:
    max = alphabet_list[i]
    max_index = i
    max_count = 1

if max_count > 1:
  print("?")
else:
  print(chr(max_index + 65))



