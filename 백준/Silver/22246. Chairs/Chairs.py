def conv(st):
    d = list(map(int,st.split(':')))
    res = d[0]*3600 + d[1]*60 + d[2]
    return res

n = int(input())
lst = [0]*(86400 + 1)
for _ in range(n):
    a,b = map(conv,input().split())
    for i in range(a,b+1):
        lst[i] += 1

print(max(lst))