
k, n = tuple(map(int, input().split()))

## k개의 랜선을 잘라서 N 개의 랜선을 만들
lines = []
for _ in range(k):
    lines.append(int(input()))

start, end = 1, max(lines)
def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2  # 중간 값 계산
        cuts = 0
        for elem in lines:
            cuts += elem // mid  # mid 길이로 잘라서 몇 개의 랜선을 만들 수 있는지 계산
        if cuts >= n:  # 만약 잘라서 만든 랜선의 수가 n 이상이라면
            result = mid  # 이 길이는 가능한 길이
            start = mid + 1  # 더 긴 길이를 찾기 위해 start를 늘려줌
        else:
            end = mid - 1  # 랜선 수가 부족하면 길이를 줄여야 함
    return result

print(binary_search(start, end))