import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

dp = [0] * 1_001

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796_796

print(dp[n])