def solution(t, p):
    answer = 0
    value = len(p)
    
    for i in range(len(t)-(value-1)):
        key = int(t[i:i+value]) 
        
        if key <= int(p):
            answer += 1
        
    return answer