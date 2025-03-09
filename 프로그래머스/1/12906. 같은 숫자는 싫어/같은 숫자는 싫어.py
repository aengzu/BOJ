def solution(arr):
    answer = []
    prev = -1
    for elem in arr:
        if prev == elem:
            continue
        else:
            answer.append(elem)
            prev = elem
    return answer