n = int(input())
lis = []
cnt = 0
i = 666
while len(lis) <= 10000:
  if '666' in str(i):
    lis.append(i)
  i += 1
  if n == len(lis):
    break
print(lis[n-1])