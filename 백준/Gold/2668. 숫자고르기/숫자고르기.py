#숫자고르기
n = int(input())
d = [0]*(n+1)
for i in range(1,n+1):
    a = int(input())
    d[i] = a

st = set()
for i in range(1,n+1):
    visit = [False]*(n+1)
    visit[i] = True

    lst = [i]
    while True:
        tmp = d[lst[-1]]
        if visit[tmp]:
            break
        
        visit[tmp] = True
        lst.append(tmp)

    if d[lst[-1]] != lst[0]: continue

    for a in lst:
        st.add(a)

print(len(st))
print(*sorted(st),sep='\n')