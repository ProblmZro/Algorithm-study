def DrawingStar(n) : 
  if n==1:
    return ['*']

  pattern = DrawingStar(n//3)
  L = []

  for i in pattern:
    L.append(i*3)
  for i in pattern:
    L.append(i+" "*(n//3)+i)
  for i in pattern:
    L.append(i*3)
  
  return L

N = int(input())
print('\n'.join(DrawingStar(N)))
# for i in range(N) : 
#   print(DrawingStar(N)[i])