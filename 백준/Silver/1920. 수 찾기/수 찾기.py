n = int(input())
an = list(map(int, input().split()))
m = int(input())
am = list(map(int, input().split()))

an.sort()

def binary_search(goal):
    ans = 0
    s, e = 0, n-1
    while s <= e:
        mid = int((s + e) / 2)
        if an[mid] == goal:
            ans = 1
            break
        if an[mid] < goal:
            s = mid + 1
        elif an[mid] > goal:
            e = mid - 1
    return ans

for elem in am:
    print(binary_search(elem))