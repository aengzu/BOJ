def solution(number):
    l = len(number)
    answer = 0
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer