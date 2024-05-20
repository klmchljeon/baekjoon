n,m = map(int,input().split())
d = list(map(int,input().split()))
lst = [max(0,d[0])]
for i in range(1,n):
    lst.append(max(0,lst[i-1] + d[i]))

cnt = 0
for i in lst:
    cnt += i >= m

print(cnt)