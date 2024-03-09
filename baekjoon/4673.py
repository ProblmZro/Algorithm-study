num_list = list(range(1, 10001))
remove_list = []

for num in range(1, 10001):
  for n in str(num):
    num += int(n)
  if num <= 10000:
    remove_list.append(num)

for i in set(remove_list):
  num_list.remove(i)

for i in num_list:
  print(i)

# for i in num_list:
#   print(i)