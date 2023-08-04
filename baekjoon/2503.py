from itertools import permutations
nums = set(permutations(['1','2','3','4','5','6','7','8','9'],3))

n = int(input())
to_remove = set()  # 삭제할 집합

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
    if not(s == strick and b == ball) :
      to_remove.add(i)
      # nums.remove(i)

nums -= to_remove  # to_remove에 있는 원소들을 nums에서 삭제

print(len(nums))