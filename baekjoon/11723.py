import sys

S = set()

for _ in range(int(sys.stdin.readline())) :
  cal =sys.stdin.readline().strip().split()
  if cal[0] == 'add':
    S.add(int(cal[1]))
  elif cal[0] == 'remove':
    S.discard(int(cal[1]))
  elif cal[0] == 'check':
    if int(cal[1]) in S : print(1)
    else : print(0)
  elif cal[0] == 'toggle':
    if int(cal[1]) in S :
      S.discard(int(cal[1]))
    else :
      S.add(int(cal[1]))
  elif cal[0] == "all":
    S = set([i for i in range(1, 21)])
  else :
    S = set()