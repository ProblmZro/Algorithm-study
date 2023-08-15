n = int(input())
stack = []
cnt = 1
canPrint = True
prlst = []

for _ in range(n):
  target = int(input())

  while cnt <= target : 
    stack.append(cnt)
    prlst.append("+")
    cnt += 1

  if stack[-1] == target :
    stack.pop()
    prlst.append("-")
  
  else: 
    canPrint = False
    break

if not canPrint : print("NO")
else : 
  for i in prlst : print(i)