def num(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())
arr = list(map(int, input().split()))

count = 0
for i in arr:
    if num(i):
        count += 1

print(count)