n = int(input())
lis = []
for _ in range(n):
  lis.append(input())
lis = list(set(lis))
lis.sort()
lis.sort(key=len)
for i in lis:
  print(i)