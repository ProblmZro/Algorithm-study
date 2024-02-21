N = sorted(list(map(int, str(input()))), reverse=True)

if sum(N) % 3 == 0:
  if 0 not in N:
    print(-1)
  else :
    print(''.join(list(map(str, N))))
else:
  print(-1)