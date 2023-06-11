#경사로
n,l = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]

v = [[False]*n for _ in range(n)]
cnt = 0
for i in range(n):
    prev = d[i][0]

    for j in range(n):
        if d[i][j] > prev:
            if d[i][j] - prev >= 2: 
                break

            tmp = prev
            if d[i][j-l:j] != [tmp]*l:
                break

            if True in v[i][j-l:j]:
                break

            v[i][j-l:j] = [True]*l

        if d[i][j] < prev:
            if prev - d[i][j] >= 2:
                break

            tmp = d[i][j]
            if d[i][j:j+l] != [tmp]*l:
                break
            
            if True in v[i][j:j+l]:
                break

            v[i][j:j+l] = [True]*l

        prev = d[i][j]

    else:
        cnt += 1

v = [[False]*n for _ in range(n)]
for j in range(n):
    prev = d[0][j]

    for i in range(n):
        if d[i][j] > prev:
            if d[i][j] - prev >= 2:
                break

            if i-l < 0: break

            tmp = prev
            flag = False
            for t in range(i-l,i):
                flag |= d[t][j]!=tmp
                flag |= v[t][j]
                v[t][j] = True

            if flag: 
                break

        if d[i][j] < prev:
            if prev - d[i][j] >= 2:
                break

            if i+l > n: break

            tmp = d[i][j]
            flag = False
            for t in range(i,i+l):
                flag |= d[t][j]!=tmp
                flag |= v[t][j]
                v[t][j] = True

            if flag: 
                break

        prev = d[i][j]

    else:
        cnt += 1

print(cnt)