#결투
n = int(input())
g = [1]*4 + [0]*(n-3)
g[0] = 0

for i in range(4,n+1):
    prev = set([g[i-3],g[i-4]])
    for j in range(i-4):
        a,b = j,i-5-j
        prev.add(g[a]^g[b])

    tmp = 0
    while tmp in prev:
        tmp += 1

    g[i] = tmp

ans = []
lst = list(input())
for i in range(n):
    if lst[i] == 'P': continue

    p1 = lst[i-2:i+1]
    p2 = lst[i-1:i+2]
    p3 = lst[i:i+3]
    for p in (p1,p2,p3):
        if p.count('P') == 2:
            ans.append(i+1)
            break

if ans:
    print('WINNING')
    print(*ans)
    exit()

gr = []
cnt = 0
idx = None
for i in range(n):
    if lst[i] == 'P': continue

    pc = lst[max(0,i-2):i+3].count('P')
    if pc == 0:
        cnt += 1
        if idx == None: idx = i

    elif cnt:
        gr.append((idx,cnt))
        cnt = 0
        idx = None

if cnt: 
    gr.append((idx,cnt))

res = 0
for _,c in gr:
    res ^= g[c]

if not res:
    print('LOSING')
    exit()

for idx,cnt in gr:
    res ^= g[cnt]

    for j in range(cnt):
        l = max(0,j-2)
        r = max(0,cnt-(j+3))
        if res^g[l]^g[r] == 0:
            ans.append(idx+j+1)

    res ^= g[cnt]

print('WINNING')
print(*ans)