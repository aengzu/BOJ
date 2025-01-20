n, m = tuple(map(int, input().split()))

bags = [ i
    for i in range(1, n+1)
]

for i in range(m):
    a, b = tuple(map(int, input().split()))
    tmp = bags[a-1]
    bags[a-1] = bags[b-1]
    bags[b-1] = tmp

for i in range(n):
    print(bags[i], end=' ')