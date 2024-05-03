n,m = map(int,input().split())
lst = list(map(int,input().split()))

s = sum(lst)

lst.sort(reverse = True)

tmp = 0
cnt = 0
for i in range(n):
    tmp += lst[i]
    cnt += 1
    
    if s-tmp <= tmp:
        break

print(m//(cnt+1))