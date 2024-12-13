import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [tuple(input().rstrip()) for _ in range(n)]
lst = tuple(lst)

dp = []
for i in range(n):
    tmp = []
    for left in range(m-1):
        right = left+1

        flag = True
        while 0<=left and right<m:
            flag &= lst[i][left]==lst[i][right]
            tmp.append(flag)

            left -= 1
            right += 1

    dp.append(tmp)

res = 0
for j in range(len(dp[0])):
    cnt = 0
    for i in range(n):
        if dp[i][j]:
            cnt += 1

        else:
            res += cnt*(cnt+1)//2
            cnt = 0

    res += cnt*(cnt+1)//2

print(res)