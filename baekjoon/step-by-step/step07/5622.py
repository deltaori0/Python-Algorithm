dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alphabets = input()

sum = len(alphabets)
for alphabet in alphabets:
  for i in range(len(dial)):
    if alphabet in dial[i]:
      sum += (i+2)

print(sum)