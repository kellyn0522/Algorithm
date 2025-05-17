n = int(input())
arr = list(map(int, input().split()))

min, max = 0, 0

for i in range(n):
    if i == 0:
        min, max = arr[i], arr[i]

    if min > arr[i]:
        min = arr[i]
    elif max < arr[i]:
        max = arr[i]

print(f"{min} {max}")