from collections import deque

a, b = tuple(map(int, input().split()))


def make_new_nums(a):
    return a * 10 + 1, a * 2


q = deque()


def bfs():
    q.append((a, 0))
    while q:
        now_num, cnt = q.popleft()
        if now_num == b:
            return cnt
        if now_num > b:
            continue

        new_num1, new_num2 = make_new_nums(now_num)
        q.append((new_num1, cnt + 1))
        q.append((new_num2, cnt + 1))
    return -2


cnt = bfs()
print(cnt + 1)
