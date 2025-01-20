n, m = tuple(map(int, input().split()))
bags = [0] * (n+1)
for i in range(m):
    a, b, c = list(map(int, input().split()))
    for k in range(a, b+1):
        bags[k] = c

for i in range(1, n+1):
    print(bags[i], end=' ')