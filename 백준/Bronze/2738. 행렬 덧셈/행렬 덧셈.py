n, m = tuple(map(int, input().split()))

ans = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(n):
    r = list(map(int, input().split()))
    for j in range(m):
        ans[i][j] += r[j]

for elem in ans:
    for e in elem:
        print(e, end=' ')
    print()