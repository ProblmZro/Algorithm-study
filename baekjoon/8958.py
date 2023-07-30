n = int(input())
for _ in range(n) :
  ans = str(input())
  score = 0
  sumS = 0
  for i in range(len(ans)) :
    if ans[i] == "O" :
      score += 1
      sumS += score
    else : score = 0
  print(sumS)