def solution(left, right):
    result = 0
    for n in range(left, right + 1):
        if int(n ** 0.5) ** 2 == n:  # 완전 제곱수 확인
            result -= n  # 홀수 개수이면 뺀다
        else:
            result += n  # 짝수 개수이면 더한다
    return result