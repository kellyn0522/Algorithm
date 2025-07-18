def solution(d, budget):
    count = 0
    sum = 0
    
    d.sort()
    for num in d:
        sum += num
        
        if sum > budget:
            return count
        
        count += 1
    
    return count