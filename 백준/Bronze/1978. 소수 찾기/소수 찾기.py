
def is_prime_num(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))
prime_nums = []

for i in range(n):
    if is_prime_num(nums[i]):
        prime_nums.append(nums[i])

print(len(prime_nums))