n = int(input())
lst = list(map(int,input()))

res = 0
cnt = 0
for i in lst:
    if i == 2:
        cnt += 1
        res += cnt*(cnt+1)//2
    else:
        cnt = 0

print(res)