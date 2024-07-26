#토마토
from collections import deque
input = iter(open(0).read().split('\n')).__next__

dw = (-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  
dv = (0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
du = (0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dt = (0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
ds = (0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dq = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0)
dp = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0)
do = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0)
dn = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0)
dm = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1)

m,n,o,p,q,r,s,t,u,v,w = map(int,input().split())
d = [[[[[[[[[[[None] for _ in range(n)] for _ in range(o)] for _ in range(p)] for _ in range(q)] for _ in range(r)] for _ in range(s)] for _ in range(t)] for _ in range(u)] for _ in range(v)] for _ in range(w)]
for _w in range(w):
    for _v in range(v):
        for _u in range(u):
            for _t in range(t):
                for _s in range(s):
                    for _r in range(r):
                        for _q in range(q):
                            for _p in range(p):
                                for _o in range(o):
                                    for _n in range(n):
                                        d[_w][_v][_u][_t][_s][_r][_q][_p][_o][_n] = list(map(int,input().split()))

queue = deque([])
cnt = 0
for _w in range(w):
    for _v in range(v):
        for _u in range(u):
            for _t in range(t):
                for _s in range(s):
                    for _r in range(r):
                        for _q in range(q):
                            for _p in range(p):
                                for _o in range(o):
                                    for _n in range(n):
                                        for _m in range(m):
                                            temp = d[_w][_v][_u][_t][_s][_r][_q][_p][_o][_n][_m]
                                            if temp == 1:
                                                queue.append((_w,_v,_u,_t,_s,_r,_q,_p,_o,_n,_m))
                                            elif temp == 0:
                                                cnt += 1

while queue:
    cw,cv,cu,ct,cs,cr,cq,cp,co,cn,cm = queue.popleft()

    for i in range(22):
        nw = cw + dw[i]
        nv = cv + dv[i]
        nu = cu + du[i]
        nt = ct + dt[i]
        ns = cs + ds[i]
        nr = cr + dr[i]
        nq = cq + dq[i]
        np = cp + dp[i]
        no = co + do[i]
        nn = cn + dn[i]
        nm = cm + dm[i]

        if 0<=nw<w and 0<=nv<v and 0<=nu<u and 0<=nt<t and 0<=ns<s and 0<=nr<r and 0<=nq<q and 0<=np<p and 0<=no<o and 0<=nn<n and 0<=nm<m and not d[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm]:
            cnt -= 1
            d[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = d[cw][cv][cu][ct][cs][cr][cq][cp][co][cn][cm] + 1
            queue.append((nw,nv,nu,nt,ns,nr,nq,np,no,nn,nm))

if cnt: 
    print(-1)
    exit()

res = 0
for _w in range(w):
    for _v in range(v):
        for _u in range(u):
            for _t in range(t):
                for _s in range(s):
                    for _r in range(r):
                        for _q in range(q):
                            for _p in range(p):
                                for _o in range(o):
                                    for _n in range(n):
                                        for _m in range(m):
                                            temp = d[_w][_v][_u][_t][_s][_r][_q][_p][_o][_n][_m]
                                            res = max(res,temp)

print(res-1)