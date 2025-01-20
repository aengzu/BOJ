
def calculate_prime_nums(n):
    ans = []
    for i in range(1, n):
        if n%i==0:
            ans.append(i)
    return ans

def is_perfect(n):
    p_nums = calculate_prime_nums(n)
    if n==sum(p_nums):
        str_pnum = str(n)+ ' = '
        for elem in p_nums:
            str_pnum += str(elem) + ' + '
        print(str_pnum[:-2])
    else:
        print(n,"is NOT perfect.")


while True:
    n = int(input())
    if n==-1:
        break
    is_perfect(n)





