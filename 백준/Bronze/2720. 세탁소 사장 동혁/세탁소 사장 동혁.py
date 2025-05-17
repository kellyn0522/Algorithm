T = int(input())
arr = [int(input()) for _ in range(T)]

Q, D, N, P = 0, 0, 0, 0

for i in range(T):
    Q = arr[i] // 25
    D = (arr[i] % 25) // 10
    N = ((arr[i] % 25) % 10) // 5
    P = ((arr[i] % 25) % 10) % 5
    print(f"{Q} {D} {N} {P}")