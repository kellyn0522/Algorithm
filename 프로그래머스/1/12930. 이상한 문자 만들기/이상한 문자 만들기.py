def solution(s):
    answer = ''
    
    word_list = s.split(' ')
    
    for words in word_list:
        for i in range(len(words)):
            if i % 2 == 0:
                answer += words[i].upper()
            else:
                answer += words[i].lower()
                
        answer += ' '
    
    return answer[:len(s)]