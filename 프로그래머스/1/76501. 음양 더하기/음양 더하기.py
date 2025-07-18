def solution(absolutes, signs):
    answer = 0
    
    for num, word in zip(absolutes, signs):
        if word == 1:
            answer += num
        else:
            cnum = -num
            answer += cnum
        
    return answer