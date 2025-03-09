def solution(d, budget):
    d.sort()
    answer = 0
    sum_d = 0
    for i in range(len(d)):
        sum_d += d[i]
        if sum_d <= budget:
            answer += 1
    return answer