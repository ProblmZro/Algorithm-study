str1 = input()
str2 = input()
w, h = len(str2), len(str1)

LCS = [[0] * (w+1) for _ in range(h+1)]

for i in range(1, h+1):
  for j in range(1, w+1):
    if str1[i-1] == str2[j-1]:
      LCS[i][j] = LCS[i-1][j-1] + 1
    else:
      LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

print(LCS[-1][-1])