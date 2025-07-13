N = input()

arr = [int(i) for i in N]
arr.sort(reverse=True)

for i in arr:
  print(i, end='')