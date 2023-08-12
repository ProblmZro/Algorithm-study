def myRound(num):
  if num - int(num) >= 0.5 : 
    return int(num) + 1
  else :
    return int(num)

n = int(input())
if n == 0 : print(0)
else : 
  stand = myRound(n * 0.15)
  dif = sorted([int(input()) for _ in range(n)])

  if stand > 0 :
    dif = dif[stand : -stand]
  
  print(myRound(sum(dif) / len(dif)))