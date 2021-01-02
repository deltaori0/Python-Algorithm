num_list = []

for i in range(9):
  num_list.append(int(input()))

max = num_list[0]
max_index = 0

for i in range(9):
  if max < num_list[i]:
    max = num_list[i]
    max_index = i

print(max, max_index+1, sep="\n")
  
