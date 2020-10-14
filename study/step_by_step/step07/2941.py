word = input()
cro_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

total = 0
for c in cro_alphabet:
  if c in word:
    word = word.replace(c, ".")

total += len(word)
print(total)