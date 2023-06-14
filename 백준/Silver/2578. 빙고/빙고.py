#빙고
def check():
    cnt = 0
    for i in range(5):
        flag = True
        for j in range(5):
            flag &= not d[i][j]

        cnt += flag

    for j in range(5):
        flag = True
        for i in range(5):
            flag &= not d[i][j]

        cnt += flag

    flag = True
    for i in range(5):
        flag &= not d[i][i]

    cnt += flag

    flag = True
    for i in range(5):
        flag &= not d[i][5-i-1]

    cnt += flag
    return cnt >= 3

a = [None]*26

d = []
for i in range(5):
    tmp = list(map(int,input().split()))
    for j in range(5):
        a[tmp[j]] = (i,j)

    d.append(tmp)

for i in range(5):
    num = list(map(int,input().split()))
    for j in range(5):
        x,y = a[num[j]]
        d[x][y] = 0
        if check():
            print(i*5+j+1)
            exit()