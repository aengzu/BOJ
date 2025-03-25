from collections import deque

n, k = tuple(map(int, input().split()))
q = deque()
ans = []

for i in range(1, n + 1):
    q.append(i)

while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    ans.append(q.popleft())

print('<' + ', '.join(map(str, ans)) + '>')