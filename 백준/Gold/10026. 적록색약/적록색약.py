from collections import deque

n = int(input())

basic_paint = [
    list(input())
    for _ in range(n)
]
c_blind_paint = [['G' if basic_paint[i][j] == 'R' else basic_paint[i][j] for i in range(n)] for j in range(n)]
visited = [[False] * n for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 상하좌우
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs(r, c, paint, visited):
    queue = deque([(r, c)])
    color = paint[r][c]
    visited[r][c] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and not visited[nx][ny] and paint[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))


basic_paint_num, c_blind_paint_num = 0, 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, basic_paint, visited)
            basic_paint_num += 1

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, c_blind_paint, visited)
            c_blind_paint_num += 1

print(basic_paint_num, c_blind_paint_num)