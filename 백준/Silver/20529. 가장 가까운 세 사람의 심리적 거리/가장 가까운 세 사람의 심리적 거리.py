#가장 가까운 세 사람의 심리적 거리
def cal(x,y,z):
    tmp = 0
    for p,q in ((x,y),(y,z),(z,x)):
        tmp += bin(p^q).count('1')

    return tmp

a = ['E','S','T','J']
b = [8,4,2,1]
dic = dict(zip(a,b))

t = int(input())
for case in range(t):
    n = int(input())
    d = list(input().split())

    cnt = [0]*16
    for i in d:
        tmp = 0
        for j in i:
            if j in dic:
                tmp += dic[j]
        
        cnt[tmp] += 1

    res = 12
    for i in range(16):
        if not cnt[i]: continue
        cnt[i] -= 1

        for j in range(16):
            if not cnt[j]: continue
            cnt[j] -= 1

            for k in range(16):
                if not cnt[k]: continue

                res = min(res,cal(i,j,k))

            cnt[j] += 1

        cnt[i] += 1

    print(res)