n = int(input())
time = [0]*(n+1)
for i in range(1,n+1):
    t,m,*lst = map(int,input().split())
    tmp = 0
    for j in lst:
        tmp = max(tmp,time[j])

    time[i] = t + tmp

print(max(time))