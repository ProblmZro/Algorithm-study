n = int(input())
for _ in range(n):
  a = list(map(str, input()))
  print(a)
  while True :
    if a[0] == ")" : 
      print("NO")
      break
    else :
      for j in range(1, len(a)):
        if a[j] == ")":
          a.pop(0)
          a.pop(j)
          print(a)
          break
    if len(a) == 0:
      print("YES")
      break
    