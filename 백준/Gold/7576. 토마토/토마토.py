from collections import deque

m, n = tuple(map(int, input().split())) # 열 행

# 토마토 배열
tomatos = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 초기 방문 배열 False 초기화
visited = [
    [False] * m
    for _ in range(n)
]

# 상 하 좌 우
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

q = deque()

# 범위 내 있는지
def in_range(x, y):
    return 0<= x < m and 0 <= y < n

def bfs():
    days = 0
    # 이미 익은 토마토 다 넣어두기
    for i in range(n):
        for j in range(m):
            if tomatos[i][j] == 1:
                q.append((j, i))
                visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and not visited[ny][nx] and tomatos[ny][nx] == 0:
                visited[ny][nx] = True
                tomatos[ny][nx] = tomatos[y][x] + 1
                days = max(days, tomatos[ny][nx])
                q.append((nx, ny))
    return days

def is_everything_riped(tomatos):
    for i in range(n):
        for j in range(m):
            if tomatos[i][j] == 0:
                return False
    return True

days = bfs()

if not is_everything_riped(tomatos):
    print(-1)
else:
    print(0 if days -1 == -1 else days - 1)