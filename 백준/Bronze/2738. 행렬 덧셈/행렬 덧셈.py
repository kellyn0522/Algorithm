N, M = map(int, input().split())

arr1 = []
for _ in range(N):
    arr1.append(list(map(int, input().split())))

arr2 = []
for _ in range(N):
    arr2.append(list(map(int, input().split())))

sum = []
for i in range(N):
    for j in range(M):
        sum.append(arr1[i][j] + arr2[i][j])
        print(sum[i*M+j], end=' ')
    print()