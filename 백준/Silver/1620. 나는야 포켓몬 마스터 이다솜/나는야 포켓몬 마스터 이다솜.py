import sys

input = sys.stdin.readline

n, m = map(int, input().split())

poketmon = {}

for i in range(1, n+1):
    data = input().rstrip()
    poketmon[data] = i
    poketmon[str(i)] = data

for _ in range(m):
    query = input().rstrip()
    print(poketmon[query])