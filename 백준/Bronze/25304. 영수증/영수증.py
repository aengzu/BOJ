x = int(input())
n = int(input())
cost = 0

for i in range(n):
    a, b = tuple(map(int, input().split()))
    cost += a*b

if cost==x:
    print('Yes')
else:
    print("No")