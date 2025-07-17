def solution(n):
    answer = []
    
    for num in str(n):
        answer.append(int(num))
    
    return answer[::-1]