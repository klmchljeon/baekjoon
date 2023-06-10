#치노의 라떼 아트 (Easy)
def conv(a,length):
    if a==0:
        return a,a+length,1
    else:
        return a,a-length,-1

s = ['#']*3 + ['.']
f = lambda x:x[1]

t = int(input())
for case in range(t):
    r,c = map(int,input().split())
    d = [list(input()) for _ in range(r)]

    for i in (0,-1):
        while d:
            if not '#' in d[i]:
                d.pop(i)
                r -= 1

            else: break

    for j in (0,-1):
        while d:
            flag = False
            for i in range(r):
                flag |= d[i][j]=='#'

            if flag: break
            
            for i in range(r):
                d[i].pop(j)

            c -= 1

    if r!=c:
        print(0)
        continue

    lst = []
    for i in (0,r-1):
        for j in (0,c-1):
            lst.append(((i,j),d[i][j]))

    lst.sort(key = f)
    
    flag = True
    for i in range(4):
        flag &= lst[i][1]==s[i]

    if not flag:
        print(0)
        continue

    x,y = lst[3][0]
    m = 0
    for i in range(*conv(x,r)):
        if d[i][y]=='#': break
        m += 1

    v = [[True]*c for _ in range(r)]
    for i in range(*conv(x,m)):
        for j in range(*conv(y,m)):
            v[i][j] = False

    flag = True
    for i in range(r):
        for j in range(c):
            flag &= (d[i][j]=='#')==v[i][j]

    print(int(flag))