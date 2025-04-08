n, m = tuple(map(int, input().split()))

em_pass_map = {}

for _ in range(n):
    email, password = input().split()
    em_pass_map[email] = password

for _ in range(m):
    print(em_pass_map[input()])

