def solution(numbers):
    sum_lst = [i for i in range(10)]
    for n in numbers:
        sum_lst[n] = 0
    return sum(sum_lst)