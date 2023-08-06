N, M = map(int, input().split())
board = []

for _ in range(N) :
  board.append(input())

def cnt_repaint(x, y):
  cnt = 0
  for i in range(x, x+8):
    for j in range(y, y+8):
      if (i+j) % 2 == 0:
        if board[i][j] != 'W':
          cnt += 1
      else :
        if board[i][j] != 'B':
          cnt += 1
  return min(cnt, 64-cnt)

min_cnt = float('inf') # 값 무한대 설정
for x in range(N - 7):
  for y in range(M - 7):
    min_cnt = min(min_cnt, cnt_repaint(x, y))
print(min_cnt)