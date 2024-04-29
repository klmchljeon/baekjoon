n = int(input())

cnt = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        if i*j > n:
            break

        cnt += 1

print(cnt)