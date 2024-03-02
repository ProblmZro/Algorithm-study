S, P = map(int, input().split())
DNA = input()
A, C, G, T = map(int, input().split())

dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
start, last = 0, P-1
first = list(DNA[start:last])
cnt = 0

for i in first:
  dic[i] += 1

while last < S:
  dic[DNA[last]] += 1

  if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
    cnt += 1
  
  dic[DNA[start]] -= 1
  start += 1
  last += 1

print(cnt)