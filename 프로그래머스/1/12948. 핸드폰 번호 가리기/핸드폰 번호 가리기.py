def solution(phone_number):
    answer = ''
    
    for word in phone_number[:-4]:
        answer += '*'

    answer += phone_number[-4:]
        
    return answer