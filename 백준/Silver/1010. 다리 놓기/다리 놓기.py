import math

t = int(input())
for i in range(t):
    n, m = tuple(map(int, input().split()))
    print(math.comb(m, n))



