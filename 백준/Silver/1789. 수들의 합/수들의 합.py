n = int(input())

sum, cnt = 0, 0

while True:
    cnt += 1
    sum += cnt

    if sum > n:
        cnt -= 1
        break

print(cnt)