from itertools import permutations
nums = list(permutations(['1','2','3','4','5','6','7','8','9'],3))

n = int(input())
lst = []
for _ in range(n):
  num, s, b = map(int, input().split())
  num = list(str(num))

  for i in nums :
    strick, ball = 0, 0
    for j in range(3) : # 0 1 2
      if num[j] == i[j] :
        strick += 1
      elif num[j] in i :
        ball += 1
    if s == strick and b == ball :  
      print(type(i))
      nums.remove(list(i))