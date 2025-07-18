
def solution(s):
    answer = ''
    
    if len(s) % 2 != 0:
        key = len(s) // 2
        answer = s[key]
    else:
        key = len(s)//2
        answer = s[key-1:key+1]
    
    return answer