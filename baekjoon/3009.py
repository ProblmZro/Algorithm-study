n = int(input())
res = 0
pri = 0

for i in range(n) : 
  a, b, c = map(int, input().split())

  if(a == b == c) :
    res = 10000 + (a * 1000)
  elif(a == b or a == c) :
    res = 1000 + (a * 100)    
  elif(b == c) :
    res = 1000 + (b * 100)
  else : 
    res = max(a, b, c) * 100

  if res > pri :
    pri = res

print(pri)