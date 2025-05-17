cnt = 0
result = []

for _ in range(10):
    a, b = map(int, input().split())
    cnt -= a
    cnt += b
    result.append(cnt)

result.sort()
print(result[-1])