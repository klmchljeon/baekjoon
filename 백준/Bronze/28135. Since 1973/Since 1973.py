n = int(input())
cnt = 0
for i in range(1,n):
    if '50' in str(i):
        cnt += 1

print(n+cnt)