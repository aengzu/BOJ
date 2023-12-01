n = int(input())
PS = []

for _ in range(n):
    flag = True
    PS = []
    s = input()
    for i in range(len(s)):
        if s[i]=='(':
            PS.append('(')
        else:
            if(len(PS)>0):
                PS.pop()
            else:
                flag = False
                break
    if len(PS) > 0:
        flag = False

    if flag:
        print("YES")
    else:
        print("NO")
