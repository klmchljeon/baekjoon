import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    prev = 0
    for i in range(n):
        a,b = lst[i],n-lst[i]+1
        if a > b: a,b = b,a

        if prev <= a:
            prev = a
            continue

        if prev <= b:
            prev = b
            continue

        break

    else:
        print('YES')
        continue

    print('NO')