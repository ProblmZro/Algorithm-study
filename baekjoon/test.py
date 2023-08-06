a = 'BWBWBWBWBW'
b = 'WBWBWBWBWB'
lst = [a, b]
cnt = 0

c = ['BWBWWWBWWW', 'WBBBWBWBBB']

for i in range(0, 9) :
  if a[i] != c[0][i] :
    cnt += 1
  if b[i] != c[1][i] :
    cnt += 1

print(cnt)