N = int(input())
minus = []
plus = []
res = 0

for _ in range(N):
  a = int(input())
  if a == 1:
    res += 1
  elif a > 0:
    plus.append(a)
  else :
    minus.append(a)

plus.sort()
minus.sort(reverse=True)

while len(plus) > 0:
  if len(plus) == 1 :
    res += plus.pop()
  else :
    res += plus.pop() * plus.pop()

while len(minus) > 0:
  if len(minus) == 1 :
    res += minus.pop()
  else :
    res += minus.pop() * minus.pop()

print(res)