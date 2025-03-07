def solution(x):
    digits_sum = sum(list(map(int, str(x))))
    return True if x % digits_sum == 0 else False