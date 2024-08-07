import sys
input = sys.stdin.read

lst = input().split('\n')
for i in lst:
    if i == '': continue
    n,b,m = map(float,i.split())
    cnt = 0
    while n <= m:
        n += b*n/100
        cnt += 1

    print(cnt)