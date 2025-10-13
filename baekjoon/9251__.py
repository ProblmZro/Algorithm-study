# dp[n][m] : s1의 1~n번째, s2의 1~m번째 문자열 LCS
s1 = input()
s2 = input()
l1, l2 = len(s1), len(s2)

dp = [[0] * (l2+1) for _ in range(l1+1)]

for n in range(1, l1+1):
  for m in range(1, l2+1):
    # 현재 비교 중인 문자가 같으면
    if s1[n-1] == s2[m-1]:
      # 이전 LCS에 +1
      dp[n][m] = dp[n-1][m-1] + 1
    # 다르면
    else:
      # 이전 LCS 중 더 큰거
      dp[n][m] = max(dp[n][m-1], dp[n-1][m])

print(dp[-1][-1])