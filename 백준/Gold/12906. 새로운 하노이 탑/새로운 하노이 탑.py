from collections import deque

di = ((0,1),(0,2),(1,2),(1,0),(2,0),(2,1))

def conv(p):
    res = []
    for i in p:
        res.append(ord(i)-ord('A'))

    return res

def tp(p):
    res = []
    for i in p:
        res.append(tuple(i))

    return tuple(res)

def check(p):
    for i in range(3):
        for j in p[i]:
            if i!=j: return False

    return True

d = []
for i in range(3):
    n,*st = input().split()
    if n == '0': 
        d.append([])
    else:
        d.append(conv(st[0]))

visitied = set()
visitied.add(tp(d))

queue = deque([(d,0)])
while queue:
    lst,t = queue.popleft()

    if check(lst):
        print(t)
        break

    for i,j in di:
        if not lst[i]: continue

        nlst = [p[:] for p in lst]
        nlst[j].append(nlst[i].pop())

        v = tp(nlst)
        if not v in visitied:
            visitied.add(v)
            queue.append((nlst,t+1))