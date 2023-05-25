n = input()
cnt = 0
while len(n) > 1:
    tmp = 1
    for i in map(int,n):
        tmp *= i

    n = str(tmp)
    cnt += 1

print(cnt)