import sys 
input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  score = [list(map(int, input().split())) for _ in range(N)]
  score.sort()
  
  cnt = 1
  tmp = score[0][1]
  for i in range(1, N):
    if tmp > score[i][1]:
      tmp = score[i][1]
      cnt += 1

  print(cnt)