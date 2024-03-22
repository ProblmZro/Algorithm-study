N = int(input())
liq = sorted(list(map(int, input().split())))

start, end = 0, N-1
ans = abs(liq[start] + liq[end])
ans_arr = [liq[start], liq[end]]

while start < end :
  curr_sum = abs(liq[start] + liq[end])

  if curr_sum < ans:
    ans = curr_sum
    ans_arr.append(liq[start])
    ans_arr.append(liq[end])
  
  if ans == 0:
    break
  
  if liq[start] + liq[end] > 0:
    end -= 1
  elif liq[start] + liq[end] < 0:
    start += 1

print(ans_arr[-2], ans_arr[-1])