t = int(input())
for _ in range(t) :
  n = int(input())
  s_list = []
  l_list = []
  for _ in range(n) :
    s,l = map(str, input().split())
    s_list.append(s)
    l_list.append(int(l))
  a = l_list.index(max(l_list))
  print(s_list[a])