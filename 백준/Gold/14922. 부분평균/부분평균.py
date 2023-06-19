#부분 평균 
max_ = 7*10**8+1

n = int(input())
d = list(map(int,input().split()))

res2 = [0,max_*2]
for i in range(n-1):
    tmp = d[i]+d[i+1]

    if res2[1] > tmp:
        res2 = [i,tmp]

res3 = [0,max_*3]
for i in range(n-2):
    tmp = d[i]+d[i+1]+d[i+2]

    if res3[1] > tmp:
        res3 = [i,tmp]

if res2[1]*3 < res3[1]*2:
    print(res2[0])
elif res2[1]*3 > res3[1]*2:
    print(res3[0])
else:
    print(min(res2[0],res3[0]))