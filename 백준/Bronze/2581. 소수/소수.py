M = int(input())
N = int(input())

def num(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum = 0
arr = []
for i in range(M, N+1):
    if num(i):
        sum += i
        arr.append(i)

if len(arr) == 0:
    print(-1)
else : 
    print(sum)
    print(arr[0])