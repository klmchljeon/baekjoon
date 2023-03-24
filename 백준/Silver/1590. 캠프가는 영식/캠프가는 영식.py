#캠프가는 영식
def check(i):
    return i >= t

n,t = map(int,input().split())
res = 1e9
for _ in range(n):
    s,i,c = map(int,input().split())

    for j in range(c):
        temp = s + i*j
        if temp >= t:
            res = min(res,temp)
            break

print(res-t if res != 1e9 else -1)