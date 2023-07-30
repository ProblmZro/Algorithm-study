n = int(input())

for i in range(n) :
  r, e, c = map(int, input().split())
  a = r + c
  b = e

  if a > b : print("do not advertise")
  elif a == b : print("does not matter")
  else : print("advertise")