n = int(input())
num = n

cnt = 0
while True:
    cnt += 1

    a = n//10
    b = n%10
    n = b*10 + (a+b)%10

    if num == n:
        break

print(cnt)