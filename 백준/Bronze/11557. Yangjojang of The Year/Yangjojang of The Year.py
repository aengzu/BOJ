t = int(input())

for i in range(t):
    n = int(input())
    s_map = {}
    for j in range(n):
        a, b = tuple(input().split())
        s_map[a] = int(b)

    max_school = max(s_map, key=s_map.get)
    print(max_school)
