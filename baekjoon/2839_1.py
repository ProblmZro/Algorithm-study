import sys
input = sys.stdin.readline

N = int(input())
sum_list = []

for x in range(N//5 + 1):
  for y in range(N//3 + 1):
    if 5*x + 3*y == N :
      sum_list.append(x+y)

if(len(sum_list) == 0) : print(-1)
else : print(min(sum_list))