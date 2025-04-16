n,q = map(int,input().split())
lst = [True]*n
for _ in range(q):
    l,i = map(int,input().split())
    for idx in range(l-1,n,i):
        lst[idx] = False

print(sum(lst))