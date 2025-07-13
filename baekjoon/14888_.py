N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
ans = []

def BackTrack(res, idx):
  if idx == N:
    ans.append(res)
    return

  if op[0] > 0:
    op[0] -= 1
    BackTrack(res + A[idx], idx+1)
    op[0] += 1

  if op[1] > 0:
    op[1] -= 1
    BackTrack(res - A[idx], idx+1)
    op[1] += 1

  if op[2] > 0:
    op[2] -= 1
    BackTrack(res * A[idx], idx+1)
    op[2] += 1

  if op[3] > 0:
    op[3] -= 1
    if res < 0 and A[idx] > 0:
      res = -(-res // A[idx])
    else:
      res = res // A[idx]
    BackTrack(res, idx+1)
    op[3] += 1

BackTrack(A[0], 1)
print(max(ans))
print(min(ans))