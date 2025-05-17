n, k = map(int, input().split())    # n : 동전의 종류 , k : 가치의 합

arr = [int(input()) for _ in range(n)]  # arr : 각 동전의 가치 

dp = [10001] * (k + 1)
dp[0] = 0

for i in range(n):
    for j in range(arr[i], k + 1):
        dp[j] = min(dp[j], dp[j - arr[i]] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])