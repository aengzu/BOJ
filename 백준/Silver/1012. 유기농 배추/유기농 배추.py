from collections import deque

t = int(input())

# 상 하 좌 우
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]



for _ in range(t):
    # m : 가로 길이 / n : 세로 길이 / k : 배추가 심어져 있는 위치의 개수
    m, n, k = list(map(int, input().split()))
    bachu = [
        [0] * m
        for _ in range(n)
    ]

    for _ in range(k):
        x, y = tuple(map(int, input().split()))
        bachu[y][x] = 1

    visited = [
        [False] * m
        for _ in range(n)
    ]

    def bfs(y, x):
        queue = deque()
        queue.append((y, x))
        visited[y][x] = True

        while queue:
            cy, cx = queue.popleft()
            for d in range(4):
                ny, nx = cy + dy[d], cx + dx[d]
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx] and bachu[ny][nx] == 1:
                        visited[ny][nx] = True
                        queue.append((ny, nx))


    ans = 0

    for i in range(n):
        for j in range(m):
            if bachu[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                ans += 1
    
    
    print(ans)