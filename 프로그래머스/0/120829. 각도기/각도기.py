def solution(angle):
    answer = 0
    answer = 1 if angle < 90 else 2 if angle == 90 else 4 if angle == 180 else 3
    return answer