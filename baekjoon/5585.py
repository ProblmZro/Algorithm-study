n = 1000 - int(input())
cnt = 0
coin = [500, 100, 50, 10, 5, 1]

for i in coin :
  cnt += n//i
  n %= i

print(cnt)