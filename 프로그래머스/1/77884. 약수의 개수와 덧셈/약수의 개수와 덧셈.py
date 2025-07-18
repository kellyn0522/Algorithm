def solution(left, right):
    answer = 0
    arr = []
    
    for num in range(left, right+1):
        for i in range(1, num+1):
            if num % i == 0:
                arr.append(i)
        
        if len(arr) % 2 == 0:
            answer += num
        else:
            answer -= num
            
        arr.clear()
        
    return answer