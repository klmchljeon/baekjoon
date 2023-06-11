#신입 사원
import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n = int(input())
    d = []
    for _ in range(n):
        a,b = map(int,input().split())
        d.append((a,b))

    d.sort()

    cnt = 0
    tmp = d[0][1]
    for i in range(1,n):
        if d[i][1] > tmp:
            cnt += 1

        else:
            tmp = d[i][1]

    print(n-cnt)