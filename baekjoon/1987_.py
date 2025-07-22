import sys
input = sys.stdin.readline

R, C = map(int, input().split())
alphabet = []
for _ in range(R):
  alphabet.append(list(input()))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# trace = [alphabet[0][0]]
trace = set()
trace.add(alphabet[0][0])

ans = 0
def dfs(x, y, res):
  global ans
  ans = max(res, ans)
  for i in range(4):
    tx = x + dx[i]
    ty = y + dy[i]
    if (0<=tx<R and 0<=ty<C) and (alphabet[tx][ty] not in trace):
        # trace.append(alphabet[tx][ty])
        trace.add(alphabet[tx][ty])
        dfs(tx, ty, res+1)
        trace.remove(alphabet[tx][ty])

dfs(0, 0, 1)

print(ans)