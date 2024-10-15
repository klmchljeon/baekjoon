import sys

lst = sys.stdin.readlines()
for input in lst:
    n,m = map(int,input.split())
    cnt = 0
    for i in range(n,m+1):
        cnt += len(str(i)) == len(set(str(i)))

    print(cnt)