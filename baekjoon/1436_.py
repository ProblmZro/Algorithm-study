res = []
i = 666
while len(res) <= 10000:
  if '666' in str(i):
    res.append(i)
  i += 1

print(res[int(input())-1])