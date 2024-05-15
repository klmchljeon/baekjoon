import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(m)]

idx = 0
res = 0
cnt = 0
for i in range(n):
    while idx < m:
        if a[i] >= b[idx]:
            cnt += b[idx]
            res += b[idx]*(i+idx+2)

            a[i] -= b[idx]
            b[idx] = 0
            idx += 1

        else:
            cnt += a[i]
            res += a[i]*(i+idx+2)

            b[idx] -= a[i]
            a[i] = 0
            break

    else:
        break
    
print(cnt,res)