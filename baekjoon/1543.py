sentence = input()
target = input()

res, i = 0, 0
while True:
  if i >= len(sentence):
    break
  if sentence[i:i+len(target)] == target:
    res += 1
    i += len(target)
  else:
    i += 1

print(res)