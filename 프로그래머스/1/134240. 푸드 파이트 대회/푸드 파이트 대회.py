def solution(food):
    answer = []
    
    for i, num in enumerate(food):
        if i == 0:
            continue
        
        cnt = num // 2
        for _ in range(cnt):
            answer.append(i)
            
    result = answer + [0] + answer[::-1]
    
    return ''.join(map(str, result))