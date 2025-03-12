def solution(numbers):
    answer = []
    l = len(numbers)
    for i in range(l-1):
        for j in range(i+1, l):
            answer.append(numbers[i] + numbers[j])
    answer = sorted(list(set(answer)))
    return answer