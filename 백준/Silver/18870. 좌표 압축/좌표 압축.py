n = int(input())
cords = list(map(int, input().split()))

set_cords = sorted(set(cords))

# 딕셔너리로 인덱스 저장
index_map = {val: idx for idx, val in enumerate(set_cords)}  # O(n)

for elem in cords:
    print(index_map[elem], end=' ')  
