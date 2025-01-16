h, m, s = list(map(int, input().split()))
cook_time = int(input())

now_s = 60*60*h + 60*m + s
end_s = now_s + cook_time

n_h = (end_s // (60*60)) % 24
n_m = (end_s % (60*60)) // 60
n_s = end_s % 60
print(n_h, n_m, n_s)