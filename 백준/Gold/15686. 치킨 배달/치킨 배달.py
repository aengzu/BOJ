from itertools import combinations

n, m = tuple(map(int, input().split()))

city_map = [
    list(map(int, input().split()))
    for _ in range(n)
]

houses, chickens = [], []
for i in range(n):
    for j in range(n):
        # 집
        if city_map[i][j] == 1:
            houses.append((i, j))
        elif city_map[i][j] == 2:
            chickens.append((i, j))

# 최소 도시 치킨 거리
min_city_chicken_distance = float('inf')

# 치킨집을 m개 고르는 모든 조합
for selected_chickens in combinations(chickens, m):
    city_chicken_distance = 0

    # 모든 집에 대해
    for hx, hy in houses:
        min_distance = float('inf')
        # 선택된 치킨집들 중 가장 가까운 거리 찾기
        for cx, cy in selected_chickens:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        city_chicken_distance += min_distance

    min_city_chicken_distance = min(min_city_chicken_distance, city_chicken_distance)

print(min_city_chicken_distance)