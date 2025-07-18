def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    
    value = min(arr)
    arr.remove(value)
    
    return arr