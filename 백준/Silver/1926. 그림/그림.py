from collections import deque

n , m = tuple(map(int, input().split()))
# n 행 m 열

paper = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 방문 여부 저장
visited = [[0] * m for _ in range(n)]
painting_cnt = 0
max_width = 0

# 상 하 좌 우
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
def in_range(ny, nx):
    return 0 <= ny < n and 0 <= nx < m

def can_go(ny, nx): # 행, 열
    if not in_range(ny, nx):
        return False
    if visited[ny][nx] == 1 or paper[ny][nx] == 0:
        return False
    return True


q = deque()
def bfs(s, e):
    global max_width
    width = 1
    q.append((s, e))
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(ny, nx):
                visited[ny][nx] = 1
                q.append((ny, nx))
                width += 1
    max_width = max(max_width, width)


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and paper[i][j] == 1:
            visited[i][j] = 1
            painting_cnt += 1
            bfs(i, j) # 행열순으로 넣기


print(painting_cnt, max_width)