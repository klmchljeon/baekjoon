n = int(input())
d = list(map(int,input().split()))

num = d[0]
cnt = 0
for i in range(n):
    if num == d[i]:
        cnt += 1

    else:
        print(*[i+1]*cnt, end = ' ')
        num = d[i]
        cnt = 1

print(*[-1]*cnt)