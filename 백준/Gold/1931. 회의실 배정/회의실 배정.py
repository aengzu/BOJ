n = int(input())

meetings = [
    list(map(int, input().split()))
    for _ in range(n)
]

checked = []
# end 시간 기준으로 오름차순 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

end = 0

for meeting in meetings:
    # 회의 시작 시간이 현재 회의 끝난 시간보다 같거나 크면
    if meeting[0] >= end:
        checked.append(meeting)
        end = meeting[1]

print(len(checked))
