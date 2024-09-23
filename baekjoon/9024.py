for _ in range(int(input())):
  n, K = map(int, input().split())
  num_list = sorted(list(map(int, input().split())))
  start, end = 0, n-1
  ans_sum = num_list[start] + num_list[end]
  ans = abs(ans_sum - K)
  cnt = 0

  while start < end:
    cur_sum = num_list[start] + num_list[end]
    cur = abs(cur_sum - K)

    if cur < ans:
      ans = cur
      cnt = 1
    elif cur == ans:
      cnt += 1

    if cur_sum < K:
      start += 1
    else:
      end -= 1
  
  print(cnt)