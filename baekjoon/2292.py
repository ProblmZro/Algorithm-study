num = int(input())
a = 1
n = 0
while True :
  a += 6 * n
  if num <= a :
    break
  n += 1
print(n + 1)