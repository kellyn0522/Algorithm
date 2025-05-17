T = int(input())
num = []

for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    num.append(arr[2])

for i in num:
    print(i)