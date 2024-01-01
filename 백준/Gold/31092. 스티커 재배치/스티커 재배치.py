n,m,k = map(int,input().split())

dic = dict() 
dic2 = dict() 

stick = [None] 
for i in range(m):
    s,d,a = input().split()
    d,a = map(int,(d,a))
    stick.append((s,d,a))

    if not s in dic:
        dic[s] = a
        dic2[s] = [i+1]
    else:
        dic[s] = min(dic[s],a)
        dic2[s].append((i+1))

mins = int(1e9)
for i in dic:
    mins = min(mins,dic[i])

b = [0] + list(map(int,input().split()))
st = input()

for i in st:
    if not i in dic:
        print(-1)
        exit()

#다 떼놓고 생각해
inven = [0]*(m+1)
for i in range(k+1,n+1):
    inven[b[i]] += 1

iinven = [0]*(m+1)
for i in range(1,k+1):
    iinven[b[i]] += 1

res = int(1e9)
for start in range(1,n-k+2):
    tmp = 0
    idx = 0
    
    inven = [0]*(m+1)
    iinven = [0]*(m+1)
    for i in range(1,start):
        inven[b[i]] += 1

    for i in range(start+k,n+1):
        inven[b[i]] += 1

    for i in range(start, start+k):
        #다른 애들을 다 빼놓자. 
        if st[idx] != stick[b[i]][0]:
            iinven[b[i]] += 1
            tmp += stick[b[i]][1]
        
        idx += 1

    idx = 0
    cnt = 0
    
    for i in range(start, start+k):
        if st[idx] == stick[b[i]][0]:
            idx += 1
            continue

        cost = 0
        flag = False
        #내부에 있었다면 그걸로 붙이고, 
        for j in dic2[st[idx]]:
            if iinven[j]:
                iinven[j] -= 1
                flag = True
                break

        if flag:
            tmp += cost
            idx += 1
            continue

        #외부에 있다면 떼오기 + 제일 싼거 붙이기
        #아니면 그냥 사오기
        t = dic[st[idx]]
        p = [int(1e9),None] 
        for j in dic2[st[idx]]: 
            if inven[j] and p[0] > stick[j][1]:
                p = [stick[j][1],j]

        if p[0] < t:
            t = p[0]
            inven[p[1]] -= 1

        cost += t
        tmp += cost
        idx += 1

    res = min(res,tmp)

print(res if res != int(1e9) else -1)