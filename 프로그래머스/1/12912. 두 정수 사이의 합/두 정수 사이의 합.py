def solution(a, b):
    answer = 0
    s = min(a, b)
    t = max(a, b)
    for i in range(s, t+1):
        answer += i
    return answer