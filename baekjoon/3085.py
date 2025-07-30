N = int(input())
board = [list(input()) for _ in range(N)]

# 사탕 최대 개수 구하기 (행, 열 따로)
def findMax():
  res, res2 = 1, 1
  for i in range(N):
    tmp, tmp2 = 1, 1
    for j in range(N-1):
      if board[i][j] == board[i][j+1]:
        tmp += 1
      elif board[i][j] != board[i][j+1]:
        res = max(res, tmp)
        tmp = 1
      if board[j][i] == board[j+1][i]:
        tmp2 += 1
      elif board[j][i] != board[j+1][i]:
        res2 = max(res2, tmp2)
        tmp2 = 1
    res = max(res, tmp)
    res2 = max(res2, tmp2)

  return max(res, res2)

ans = 0
for x in range(N):
  for y in range(N-1):
    for dx, dy in [(1, 0), (0, 1)]:
      nx = x + dx
      ny = y + dy
      if nx < N and ny < N:
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
        ans = max(ans, findMax())
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y] # 원래대로

print(ans)

# print(res)

# for i in range(0, N-1):
#   for j in range(0, N-1):
#     tmp_board = board
#     tmp = tmp_board[i][j]
#     tmp_board[i][j] = tmp_board[i][j+1]
#     tmp_board[i][j+1] = tmp

