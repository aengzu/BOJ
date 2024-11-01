
def get_input_nums():
    nums = list(map(int, input().split()))
    return nums

def get_avg_nums(nums_array):
    sum_nums = sum(nums_array)
    len_nums = len(nums_array)
    return sum_nums / len_nums

def print_format_result(test_case, avg):
    rounded_avg = round(avg)  # 소수점 첫째 자리에서 반올림한 정수로 변환
    print(f'#{test_case} {rounded_avg}')
    return

def simulate(T):
    for test_case in range(1, T+1):
        seqs = get_input_nums()
        avg_num = get_avg_nums(seqs)
        print_format_result(test_case, avg_num)
    return

if __name__ == '__main__':
    T = int(input())
    simulate(T)




