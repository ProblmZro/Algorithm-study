N = int(input())
M = N
cnt = 0

while True:
  M = (M%10)*10 + (M%10 + M//10)
  cnt += 1
  if M == N :
    break

print(cnt)