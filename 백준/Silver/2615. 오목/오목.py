
# 바둑판 입력 받기
checkboard = [
    list(map(int, input().split()))
    for _ in range(19)
]

# 배열 한 줄 검사
def check_line(line):
    if not line:  # 빈 리스트 예외 처리
        return 0, 0
    prev, winner = line[0], 0
    cnt = 0
    for idx, l in enumerate(line):
        # 만약 이전과 연속된 녀석이라면 연속 개수 세기
        if prev == l and l != 0:
            cnt += 1
            winner = l
        # 다른 녀석이면 초기화
        else:
            cnt = 1
            winner = 0
        prev = l
        # 만약 오목이면
        if cnt == 5:
            # 만약 육목이면
            if idx + 1 < len(line) and line[idx+1] == l:
                continue
            else:
                return winner, idx
    return 0, 0

def get_diagols(board, direction):
    ans = []
    # \ 방향일 때 r + c 가 같으면 같은 대각선
    if direction == 'r':
        for s in range(-18, 19):
            diag = [board[r][c] for r in range(19) for c in range(19) if r - c == s]
            ans.append(diag)
    # / 방향일 때 : r - c  가 같으면 같은 대각선
    elif direction == 'l':
        for s in range(0, 38):
            diag = [board[r][c] for r in range(19) for c in range(19) if r + c == s]
            ans.append(diag)
    return ans

def get_winner(board):
    winner = 0
    # 가로 줄 완탐
    for row, r in enumerate(board):
        winner, col = check_line(r)
        if winner != 0:
            return winner, row, col-4
    # 세로 줄 완탐
    for col, c in enumerate(zip(*board)):
        winner, row = check_line(list(c))
        if winner != 0:
            return winner, row-4, col
    # 대각선 줄 완탐 \
    for idx, d in enumerate(get_diagols(checkboard, direction='r')):
        winner, c = check_line(d)
        r = abs(18 - idx) + c
        if winner != 0:
            return winner, r-4, c-4
    # 대각선 완탐 /
    for idx, d in enumerate(get_diagols(checkboard, direction='l')):
        winner, r = check_line(d)
        c = idx - r
        if winner != 0:
            return winner, r, c
    return winner, -1, -1


w, r, c = get_winner(checkboard)
if w == 0:
    print(0)
else:
    print(f"{w}\n{r+1} {c+1}")