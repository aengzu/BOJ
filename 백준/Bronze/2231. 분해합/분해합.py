
def find_decomp_sum(n):
    # case 1)
    if n <= 18:
        if n % 2 ==0:
            return int(n/2)
    # case 2)
    num_len = len(str(n))
    for i in range(1, n):
        dis_sum = i
        tmp = i
        for pos in range(num_len, 0, -1):
            dis_sum += tmp// (10**(pos-1))
            tmp %= (10**(pos-1))
        if dis_sum == n:
            return i
    return 0



# case 1) n 이 한자리수
## 9 의 분해합 9+9 = 18, 1의 분해합 1+1 = 2, 2의 분해합 = 2+2= 4 -> 2*n

# case 2) n 의 두자리수 이상
## 10 의 분해합 10 + 1 = 11, 14의 분해합 1+4+14 = 19 등 직접 구해야함 범위는 (n < 분해합 < n+9*자릿수)

n = int(input())
print(find_decomp_sum(n))