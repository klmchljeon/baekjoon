import sys
input = sys.stdin.readline

n,q = map(int,input().split())
row = [0]*n
col = [0]*n
res = n**2
a,b = n,n
for _ in range(q):
    query,num = input().split()
    idx = int(num) - 1

    if query == 'ROW':
        if 0 <= idx-1:
            if row[idx-1] == row[idx]:
                res -= a
                b -= 1

            else:
                res += a
                b += 1

        if idx+1 < n:
            if row[idx] == row[idx+1]:
                res -= a
                b -= 1

            else:
                res += a
                b += 1

        row[idx] ^= 1

    else:
        if 0 <= idx-1:
            if col[idx-1] == col[idx]:
                res -= b
                a -= 1

            else:
                res += b
                a += 1

        if idx+1 < n:
            if col[idx] == col[idx+1]:
                res -= b
                a -= 1

            else:
                res += b
                a += 1

        col[idx] ^= 1

    print(res)