lst = list(map(int,input().split()))
p = max(lst)
if p in lst[:-1]:
    print(p+1)
else:
    print(p)