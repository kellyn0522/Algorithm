def solution(s):
    answer = True
    
    sum1 = s.count('p') + s.count('P')
    sum2 = s.count('y') + s.count('Y')

    return sum1 == sum2