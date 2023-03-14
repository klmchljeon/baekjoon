dic = [{"java":0,"python":1,"cpp":2},
       {"backend":0,"frontend":1},
       {"junior":0,"senior":1},
       {"chicken":0,"pizza":1}]

lst = [[[[[] for i3 in range(2)] for i2 in range(2)] for i1 in range(2)] for i0 in range(3)]

leng = [3,0,2,0,2,0,2]

def find(a,b,c,d,num):
    lenn = len(lst[a][b][c][d])
    s,e = -1,lenn
    while s+1<e:
        mid = (s+e)//2
        
        if lst[a][b][c][d][mid] < num:
            s = mid
        else:
            e = mid

    return lenn - (s+1)

def convq(st):
    tmp = st.split()
    res = []
    for i in range(0,7,2):
        if tmp[i] == '-':
            res.append(list(range(leng[i])))
        else:
            res.append([dic[i//2][tmp[i]]])
    
    res.append(int(tmp[7]))
    
    return res
            
def convi(st):
    tmp = st.split()
    res = []
    for i in range(4):
        res.append(dic[i][tmp[i]])
    
    res.append(int(tmp[4]))
    return res

def solution(info, query):
    answer = []
    
    for i in info:
        a,b,c,d,e = convi(i)
        lst[a][b][c][d].append(e)
    
    for i0 in range(3):
        for i1 in range(2):
            for i2 in range(2):
                for i3 in range(2):
                    lst[i0][i1][i2][i3].sort()
    
    for i in query:
        cnt = 0
        a,b,c,d,score = convq(i)
        for i0 in a:
            for i1 in b:
                for i2 in c:
                    for i3 in d:
                        cnt += find(i0,i1,i2,i3,score)
                        
        answer.append(cnt)
    
    return answer