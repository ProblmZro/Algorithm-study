while True:
  try:
    n = int(input())
  except:
    break
  i, ans = 1, 1
  while True:
    if i >= n and i % n == 0:
      print(ans)
      break
    ans += 1
    i = i * 10 + 14