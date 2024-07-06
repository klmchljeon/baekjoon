n = int(input())
lst = list(map(int,input().split()))

res = 0
cur = 0
while lst:
    p = lst.pop()
    cur = min(cur+1,p)
    res += cur
    
print(res)