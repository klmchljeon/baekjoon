#국기 인식
def hor(s,e):
    dic = dict(zip(al,[0]*26))
    for i in range(s,e):
        for j in range(9):
            st = d[i][j]
            dic[st] += 1

    res = sorted(dic.items(),key=f)[:3]
    return res

def ver(s,e):
    dic = dict(zip(al,[0]*26))
    for i in range(6):
        for j in range(s,e):
            st = d[i][j]
            dic[st] += 1

    res = sorted(dic.items(),key=f)[:3]
    return res

def cal(lst):
    res = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                fir = lst[0][i][0] == lst[1][j][0]
                sec = lst[1][j][0] == lst[2][k][0]
                if fir or sec: continue

                cnt = lst[0][i][1] + lst[1][j][1] + lst[2][k][1]
                res = max(res,cnt)

    return 54 - res

al = [chr(i+ord('A')) for i in range(26)]
f = lambda x:-x[1]

d = [input() for _ in range(6)]

h = [hor(i,i+2) for i in range(0,6,2)]
v = [ver(i,i+3) for i in range(0,9,3)]

print(min(cal(h),cal(v)))