from itertools import combinations

def solution(numbers):
    answer = []
    
    combi = combinations(numbers, 2)
    
    for nums in combi:
        answer.append(sum(nums))
        
    answer = sorted(list(set(answer)))
    
    return answer