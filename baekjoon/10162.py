t = int(input())
a = 0
b = 0
c = 0
if (t >= 300) :
  a = t // 300
  t -= 300 * a

if (t >= 60) : 
  b = t // 60
  t -= 60 * b

if (t >= 10) : 
  c = t // 10
  t -= 10 * c

if(t == 0) :
  print(a, b, c)

else :
  print(-1)