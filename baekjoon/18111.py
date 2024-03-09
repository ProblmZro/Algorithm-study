# import sys
# input = sys.stdin.readline

# N, M, B = map(int, input().split())
# land = [list(map(int, input().split())) for _ in range(N)]
# time, height = int(1e9), 0

# for floor in range(257):
#   in_block, out_block = 0, 0

#   for i in range(N):
#     for j in range(M):
      
#       if floor < land[i][j]:
#         out_block += land[i][j] - floor
#       else:
#         in_block += floor - land[i][j]
  
#   if in_block > out_block + B :
#     continue
  
#   cnt = 2 * (out_block) + in_block

#   if cnt <= time:
#     time = cnt
#     height = floor

# print(time, height)

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

data = [0] * 257

for row in land:
    for height in row:
        data[height] += 1

out_block = sum(i * data[i] for i in range(257))
in_block = 0
ans = (out_block * 2, 0)
t = data[0]

for i in range(1, 257):
    in_block += t
    out_block -= N * M - t
    t += data[i]

    if out_block + B < in_block:
        break
    else:
        ans = min((out_block * 2 + in_block, -i), ans)

print(ans[0], -ans[1])