n = int(input())
sum_list = []
for x in range(n//3+1):
  for y in range(n//3+1):
    if 3 * x + 5 * y == n:
      sum_list.append(x+y)

if len(sum_list) == 0 :
  print(-1)
else : print(min(sum_list))