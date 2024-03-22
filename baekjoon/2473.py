N = int(input())
liq = sorted(list(map(int, input().split())))
ans_arr = [liq[0], liq[1], liq[N-1]]
ans = abs(liq[0] + liq[1] + liq[N-1])

for mid in range(N-2):
  start, end = mid+1, N-1
  while start < end :
    curr_sum = abs(liq[start] + liq[mid] + liq[end])

    if curr_sum < ans:
      ans = curr_sum
      ans_arr = [liq[mid], liq[start], liq[end]]
    
    if ans == 0:
      break
    
    if liq[start] + liq[mid] + liq[end] > 0:
      end -= 1
    elif liq[start] + liq[mid] + liq[end] < 0:
      start += 1

print(ans_arr[-3], ans_arr[-2], ans_arr[-1])