n = int(input())
scr1 = 100
scr2 = 100
for _ in range(n) :
  a, b = map(int, input().split())
  if a > b :
    scr2 -= a
  elif b > a :
    scr1 -= b
print(scr1)
print(scr2)