num = int(input())
isThere = 0
for i in range(num) :
  if i + sum(map(int, str(i))) == num :
    print(i)
    isThere += 1
    break
if isThere == 0 :
  print(0)