n = int(input())
t = 30
cnt = 0
for i in range(n):
    a = int(input())
    if t > a:
        t -= a
        cnt += 1
    else:
        cnt += t*2 >= a
        t = 30

print(cnt)