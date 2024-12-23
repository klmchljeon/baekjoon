n,m = map(int,input().split())
lst = list(map(int,input().split()))

lst.sort(key = lambda x:(x%10,x),reverse = True)

cnt = 0
while lst:
    if lst[-1] <= 10: 
        cnt += lst.pop()==10
        continue

    if not m: break

    lst[-1] -= 10
    m -= 1
    cnt += 1

print(cnt)