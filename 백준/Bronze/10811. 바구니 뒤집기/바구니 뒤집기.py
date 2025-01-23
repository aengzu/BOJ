n, m = tuple(map(int, input().split()))

bags = [
    i for i in range(1, n+1)
]

for _ in range(m):
    i, j = tuple(map(int, input().split()))
    tmp = bags[i-1: j]
    tmp.reverse()
    bags[i-1:j] = tmp

for i in range(n):
    print(bags[i], end=' ')