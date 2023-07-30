isTrue = False
dwfs = []

for _ in range(9):
 dwfs.append(int(input()))
 
for i in range(8) :
  if isTrue :
    break
  for j in range(i+1, 9) : 
    if sum(dwfs) - dwfs[i] - dwfs[j] == 100 :
      dwfs.pop(i)
      dwfs.pop(j-1)
      isTrue = True
      break

for dwf in dwfs:
  print(dwf)