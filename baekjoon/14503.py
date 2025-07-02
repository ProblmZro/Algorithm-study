N, M = map(int, input().split())
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

room = []
res = 0
for _ in range(N):
  room.append(list(map(int, input().split())))

x, y = r, c

while True:
  # 현재 위치 더러우면 청소
  if room[x][y] == 0:
    room[x][y] = 2  
    res += 1
    isDirty = False

  for _ in range(4):
    d = (d + 3) % 4 # 반시계 회전
    tx = x + dx[d]
    ty = y + dy[d]
    # 더러운 곳 있다면 그곳을 이동
    if 0 <= tx < N and 0 <= ty < M and room[tx][ty] == 0:
      isDirty = True
      x, y = tx, ty
      break

  if not isDirty:
    back = (d + 2) % 4 # 뒤로 회전 (방향 d 유지)
    bx = x + dx[back]
    by = y + dy[back]
    # 더러운 곳 없다면 뒤로 한 칸 후진
    if 0 <= bx < N and 0 <= by < M and room[bx][by] != 1:
      x, y = bx, by
    else:
      break

print(res)