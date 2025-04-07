import sys

sys = sys.stdin

n = int(sys.readline())

time_p = list(map(int, sys.readline().split()))

time_p.sort()
result = 0

for idx, x in enumerate(time_p):
    result += (n-idx) * x

print(result)