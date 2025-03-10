from collections import deque


def find_goal(grid):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                return (i, j)  # (행, 열)
    return None


def in_range(x, y):
    return 0 <= x < m and 0 <= y < n


def can_go(x, y):
    if not in_range(x, y):
        return False
    if grid[y][x] == 0:
        return False
    return True


n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)]

goal_idx = find_goal(grid)

# dir = 왼, 오, 아, 위
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
distances = [
    [-1] * m for _ in range(n)
]


def bfs():
    q = deque()
    q.append(goal_idx)
    visited[goal_idx[0]][goal_idx[1]] = True
    distances[goal_idx[0]][goal_idx[1]] = 0

    while q:
        y, x = q.popleft()  # 행과 열
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if can_go(nx, ny) and not visited[ny][nx]:
                visited[ny][nx] = True
                distances[ny][nx] = distances[y][x] + 1
                q.append((ny, nx))


bfs()

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            distances[i][j] = 0

# 결과 출력
for row in distances:
    print(*row)
