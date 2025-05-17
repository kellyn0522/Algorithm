h, w = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0

for i in range(1, w-1):
    left = max(arr[:i])
    right = max(arr[i+1:])
    cnt = min(left, right)

    if cnt > arr[i]:
        sum += cnt - arr[i]

print(sum)