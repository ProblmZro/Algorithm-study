case = int(input())

for i in range(case) :
  m, s = map(str, input().split())
  m = int(m)
  for j in range(len(s)) :
    print(s[j] * m, end='')
  print('')