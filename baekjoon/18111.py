import sys

N, M, B = map(int, sys.stdin.readline().split())
land = []
for _ in range(N):
  land.append(list(map(int, sys.stdin.readline().split())))
time, height = int(1e9), 0

for i in range(257):
  in_block = 0
  out_block = 0
  for j in range(N):
    for k in range(M):
      if i < land[j][k]:
        out_block += land[j][k] - i
      else:
        in_block += i - land[j][k]
  if in_block > out_block + B :
    continue
  cnt = 2 * (out_block) + in_block

  if cnt <= time:
    time = cnt
    height = i

print(time, height)