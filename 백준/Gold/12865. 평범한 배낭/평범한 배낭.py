n, k = tuple(map(int, input().split()))

dp = [0] * (k+1)
items = []
for _ in range(n):
    w, v = tuple(map(int, input().split()))
    items.append((w,v))

for item in items:
    w, v = item
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])