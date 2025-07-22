def solution(s, n):
    answer = ''
    
    for i in range(len(s)):
        if s[i].isspace():
            answer += ' '
            continue
        
        num = ord(s[i])
        if num <= 90 and num + n >= 91: # 소문자 : 65 - 90
            answer += chr(num + n - 26)
        elif num >= 97 and num + n >= 123: # 대문자 : 97 - 122
            answer += chr(num + n - 26)
        else: 
            answer += chr(num + n)
    
    return answer