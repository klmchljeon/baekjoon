n = int(input())

cnt = 0
for i in range(n-4):
    for j in range(i+1,n-3):
        for k in range(j+1,n-2):
            for l in range(k+1,n-1):
                for m in range(l+1,n):
                    cnt += 1

print(cnt)