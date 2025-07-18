def solution(n):
    answer = 0
    num_list = []
    
    # 10진법 수 n을 3진법 수로 변경 
    while n > 0:
        num_list.append(n % 3)
        if n != 1:
            n = n // 3
        else:
            break
            
    num_list.reverse()
    
    for i, key in enumerate(num_list):
        answer += ((3**i) * key)
    
    return answer