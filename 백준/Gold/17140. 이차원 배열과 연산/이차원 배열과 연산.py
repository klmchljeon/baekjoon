#이차원 배열과 연산
d = [[0]*100 for _ in range(100)]

f = lambda x:(x[1],x[0])

r,c,k = map(int,input().split())
r-=1; c-=1
for i in range(3):
    tmp = list(map(int,input().split()))
    for j in range(3):
        d[i][j] = tmp[j]

row = 3
cal = 3

sec = 0
while d[r][c] != k:
    if row >= cal:
        lencal = []

        for i in range(row):
            dic = dict()
            for j in range(cal):
                if not d[i][j]: continue

                if d[i][j] in dic:
                    dic[d[i][j]] += 1
                else:
                    dic[d[i][j]] = 1

            tmp = sorted(dic.items(),key=f)

            lst = []
            for key,val in tmp:
                lst.append(key)
                lst.append(val)

            t = min(len(lst),100)
            for j in range(t):
                d[i][j] = lst[j]

            lencal.append(t)

        cal = max(lencal)
        for i in range(row):
            for j in range(lencal[i],cal):
                d[i][j] = 0

    else:
        lenrow = []

        for j in range(cal):
            dic = dict()
            for i in range(row):
                if not d[i][j]: continue

                if d[i][j] in dic:
                    dic[d[i][j]] += 1
                else:
                    dic[d[i][j]] = 1

            tmp = sorted(dic.items(),key=f)
            lst = []
            for key,val in tmp:
                lst.append(key)
                lst.append(val)

            t = min(len(lst),100)
            for i in range(t):
                d[i][j] = lst[i]

            lenrow.append(t)

        row = max(lenrow)
        for j in range(cal):
            for i in range(lenrow[j],row):
                d[i][j] = 0       

    sec += 1

    if sec == 101: break

print(sec if sec <= 100 else -1)