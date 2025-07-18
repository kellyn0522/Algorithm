def solution(seoul):
    answer = ''
    
    for i, word in enumerate(seoul):
        if word == "Kim":
            return f"김서방은 {i}에 있다"
            