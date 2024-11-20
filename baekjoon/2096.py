N = int(input())
arr = list(map(int, input().split()))

dp_max = arr
dp_min = arr

for _ in range(N-1):
  arr = list(map(int, input().split()))
  dp_max = [max(dp_max[0], dp_max[1]) + arr[0], max(dp_max) + arr[1], max(dp_max[1], dp_max[2]) + arr[2]]
  dp_min = [min(dp_min[0], dp_min[1]) + arr[0], min(dp_min) + arr[1], min(dp_min[1], dp_min[2]) + arr[2]]

print(max(dp_max), min(dp_min))


# dp_max = [[0, 0, 0] for _ in range(N)]
# dp_min = [[0, 0, 0] for _ in range(N)]
# dp_max[0][:3] = arr[0][:3]
# dp_min[0][:3] = arr[0][:3]

# for i in range(1, N):
#   dp_max[i][0] = max(dp_max[i-1][0], dp_max[i-1][1]) + arr[i][0]
#   dp_max[i][1] = max(dp_max[i-1][0], dp_max[i-1][1], dp_max[i-1][2]) + arr[i][1]
#   dp_max[i][2] = max(dp_max[i-1][1], dp_max[i-1][2]) + arr[i][2]

# for i in range(1, N):
#   dp_min[i][0] = min(dp_min[i-1][0], dp_min[i-1][1]) + arr[i][0]
#   dp_min[i][1] = min(dp_min[i-1][0], dp_min[i-1][1], dp_min[i-1][2]) + arr[i][1]
#   dp_min[i][2] = min(dp_min[i-1][1], dp_min[i-1][2]) + arr[i][2]

# print(max(dp_max[-1][0:3]), min(dp_min[-1][0:3]))
