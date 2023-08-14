import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
  num_list.append(int(input()))
num_list.sort()

print(round(sum(num_list) / len(num_list)))
print(num_list[len(num_list)//2])

count = Counter(num_list)
mode = count.most_common()
if len(mode) > 1 and mode[0][1] == mode[1][1] :
  print(mode[1][0])
else : 
  print(mode[0][0])

print(max(num_list) - min(num_list))