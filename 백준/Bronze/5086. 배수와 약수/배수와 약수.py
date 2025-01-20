
def classify(n1, n2):
    if n1 % n2 == 0:
        return 'multiple'
    elif n2 % n1 == 0:
        return 'factor'
    else:
        return 'neither'

while True:
    a, b = tuple(map(int, input().split()))
    if a==0 and b ==0:
        break
    print(classify(a, b))
