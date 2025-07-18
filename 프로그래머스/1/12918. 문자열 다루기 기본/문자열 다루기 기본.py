import re

def solution(s):
    
    if len(s) == 4 or len(s) == 6:
        if re.match(r'^\d+$', s):
            return True
        
    return False