from collections import deque

# m : 열 / n : 행 / h : 높이
m, n, h = list(map(int, input().split()))

# 토마토 배열
totmatos = [[
    list(map(int, input().split()))
    for _ in range(n)
] for _ in range(h)]
# 방문 여부 저장 배열
visited = [[[False] * m for _ in range(n)]
           for _ in range(h)]

# 왼 오 위 아 앞 뒤
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
q = deque()

def in_range(x, y, z):
    return 0 <= x < m and 0 <= y < n and 0 <= z < h


def bfs():
    while q:
        z, y, x = q.popleft()
        # [왼 오 위 아 앞 뒤] 토마토 순회
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            # 범위 안에 있고, 방문 한 적 없고, -1 이 아니라면 방문 후 day 업데이트 후 큐에 넣기
            if in_range(nx, ny, nz) and not visited[nz][ny][nx] and totmatos[nz][ny][nx] != -1:
                visited[nz][ny][nx] = True
                totmatos[nz][ny][nx] = totmatos[z][y][x] + 1
                q.append((nz, ny, nx))


# 시작 지점 좌표들 (h, 행, 열) 큐에 넣기
for i in range(h):
    for j in range(n):
        for k in range(m):
            if totmatos[i][j][k] == 1:
                q.append((i, j, k))
                visited[i][j][k] = True

# 탐색하면서 day 업데이트
bfs()

# 만약 한번도 못간 토마토 있다면, days = -1 그게 아니라면 max 값 리턴
def get_days():
    days = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if totmatos[i][j][k] == 0:
                    return -1
                else:
                    days = max(totmatos[i][j][k], days)
    return days - 1



print(get_days())
