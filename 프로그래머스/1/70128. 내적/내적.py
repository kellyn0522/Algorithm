def solution(a, b):
    n = len(a)
    sum = 0
    
    for num1, num2 in zip(a, b):
        sum += num1 * num2
    
    return sum