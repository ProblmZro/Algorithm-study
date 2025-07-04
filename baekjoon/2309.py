mini = []
for _ in range(9):
  mini.append(int(input()))
mini.sort()
sum_mini = sum(mini)

for i in range(0, 8):
  for j in range(i+1, 9):
    if sum_mini-mini[i]-mini[j] == 100:
      for k in range(0, 9):
        if k != i and k != j:
          print(mini[k])
      exit()