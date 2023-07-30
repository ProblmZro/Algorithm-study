n = int(input())
x = 0
y = 0

for i in range(n) :
  a = int(input())
  if a == 1 : x += 1
  elif a == 0 : y += 1

if x > y : print("Junhee is cute!")
elif y > x : print("Junhee is not cute!")