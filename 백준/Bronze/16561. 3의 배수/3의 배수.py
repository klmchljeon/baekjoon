n = int(input())
n = n//3
cnt = 0
for i in range(1,n-1):
    for j in range(1,n-i):
        k = n-i-j
        cnt += 1

print(cnt)