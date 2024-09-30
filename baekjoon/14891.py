from collections import deque

def right(n, d):
  if n > 3: return
  if wheel[n-1][2] != wheel[n][6]:
    right(n+1, -d)
    wheel[n].rotate(d)

def left(n, d):
  if n < 0: return
  if wheel[n][2] != wheel[n+1][6]:
    left(n-1, -d)
    wheel[n].rotate(d)

wheel = [deque(list(map(int,input()))) for _ in range(4)]

for _ in range(int(input())):
  n, d = map(int,input().split())
  n -= 1

  left(n-1, -d)
  right(n+1, -d)
  wheel[n].rotate(d)

score = 0
for i in range(4):
  if wheel[i][0] == 1:
    score += 2 ** i

print(score)