def solution(s):
    if len(s) % 2 ==0:
        l = int(len(s)/2)
        return s[l-1:l+1]
    else:
        return s[int(len(s)/2)]