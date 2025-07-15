N = int(input())
liq = list(map(int, input().split()))
start, end = 0, N-1
liq.sort()

res = 10e9
while start < end:
  liq_sum = liq[start] + liq[end]
  if abs(liq_sum) < res:
    res = abs(liq_sum)
    a, b = liq[start], liq[end]

  if liq_sum > 0:
    end -= 1
  else :
    start += 1

print(a, b)


# -5 -3 2 3

# 5 2