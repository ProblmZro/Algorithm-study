import sys
n = int(sys.stdin.readline())
dp = [0, 1]

for i in range(2, n+1) :
    dp.append(min([dp[i-(j**2)]+1 for j in range(1, int(i**0.5)+1)]))

print(dp[n])
# dp[1] = 1  
# dp[2] = 2
# dp[3] = 3
# dp[4] = 2^2 -> 1
# dp[5] = 1^2 + 2^2 -> 2
# dp[13] = 3^2 + 2^2 -> 2 / dp[13] = dp[3^2] + dp[2^2]

# 13-1 = 12 -> 1
# 13-4 = 9 -> 1
# 13-9 = 4 -> 1