def solution(n):
    answer = 0
    l = len(str(n))
    for i in range(l-1, -1, -1):
        answer += n // (10**i)
        n = n % (10**i)
    return answer