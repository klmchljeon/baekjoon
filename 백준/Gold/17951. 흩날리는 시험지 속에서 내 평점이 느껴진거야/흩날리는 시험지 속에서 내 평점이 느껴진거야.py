#흩날리는 시험지 속에서 내 평점이 느껴진거야
def check(num):
    cnt = 0
    tmp = 0
    for i in d:
        tmp += i
        if tmp >= num:
            tmp = 0
            cnt += 1

    return cnt >= k

n,k = map(int,input().split())
d = list(map(int,input().split()))

s,e = 0,int(20e5)+1
while s+1<e:
    mid = (s+e)//2

    if check(mid):
        s = mid

    else:
        e = mid

print(s)