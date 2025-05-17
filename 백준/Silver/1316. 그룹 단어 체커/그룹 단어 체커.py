N = int(input())
arr = [input() for _ in range(N)]

for i in range(N):
    for j in range(len(arr[i])-1):
        if arr[i][j] == arr[i][j+1]:
            pass
        else:
            if arr[i][j] in arr[i][j+1:]:
                N -= 1
                break

print(N)