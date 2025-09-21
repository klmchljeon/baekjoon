#근성아 일 좀 하자
import sys
from heapq import *
input = sys.stdin.readline
max_ = int(1e18)

class trash:
    def __init__(self,loc,w,di,len = 2,t = 0):
        self.head = loc
        self.w = w
        self.di = di
        self.len = len
        self.t = t
        return
    
    @property
    def tail(self):
        return self.head + self.len
 
    def __lt__(self,other):
        return self.head < other.head
    
    def __str__(self):
        d = ['0','R','L']
        w = f"{self.w}" if self.w < max_ else "inf"
        return f"[{self.head}~{self.tail}/d={d[self.di]}/w={w}/t={self.t}]"
 
#충돌 여부 판정
def is_crash(a,b):
    d1 = lst[a].di
    d2 = lst[b].di
    if d1 == d2:
        return False
    
    if d1 == -1 or d2 == 1:
        return False
    
    return True
 
#충돌이 발생하는 글로벌 시간, 그때의 t1.head (충돌은 보장된 상태)
def move(t1:trash,t2:trash):
    #t2가 이동
    if t1.di == 0:
        dist = t2.head - t1.tail
        t = t2.t + dist
        loc = t1.head
 
    #t1이 이동
    elif t2.di == 0:
        dist = t2.head - t1.tail
        t = t1.t + dist
        loc = t1.head + dist
 
    #둘다 이동
    else:
        init_t = max(t1.t,t2.t)
        #시간대에 맞는 위치 loc1은 t1의 오른쪽 끝, loc2는 t2의 왼쪽 끝
        loc1 = t1.tail + max(0, t2.t - t1.t)
        loc2 = t2.head - max(0, t1.t - t2.t)

        dist = (loc2 - loc1)//2
        t = init_t + dist
        loc = (loc1-t1.len) + dist

    return t,loc
 
def update(a,b):
    if a == None or b == None: return
    if not is_crash(a,b): return 
 
    t,loc = move(lst[a],lst[b])
    heappush(heap,(t,loc,(a,b),(lst[a].len,lst[b].len))) #예비 충돌 당시의 길이를 기록(유효성 검사용)
 
def merge2(t,loc,idx):
    a,b = idx
    v[b] = False
    #a의 오른쪽은 b의 오른쪽으로, 해당 인덱스의 왼쪽을 다시 a로
    if adj[b][1] != None:
        adj[a][1] = adj[b][1]
        adj[adj[a][1]][0] = a
 
    t1 = lst[a]
    t2 = lst[b]
 
    if t1.w > t2.w:
        di = t1.di
 
    elif t1.w < t2.w:
        di = t2.di
 
    else:
        di = 0
 
    lst[a] = trash(loc, t1.w+t2.w, di, t1.len+t2.len, t)
    return

def merge3(t,loc,idx):
    a,b,c = idx
    v[b] = False
    v[c] = False

    #a의 오른쪽은 c의 오른쪽으로, 해당 인덱스의 왼쪽을 다시 a로
    if adj[c][1] != None:
        adj[a][1] = adj[c][1]
        adj[adj[a][1]][0] = a

    t1 = lst[a]
    t2 = lst[b]
    t3 = lst[c]

    if t1.w == t3.w or (t1.w <= t2.w and t3.w <= t2.w):
        di = 0

    elif t1.w > t3.w:
        di = t1.di

    else:
        di = t3.di

    lst[a] = trash(loc, t1.w+t2.w+t3.w, di, t1.len+t2.len+t3.len, t)
    return

#충돌 유효성 검사
def check(idx,size):
    a,b = idx
    sa,sb = size
    if not (v[a] and v[b]): return False
    if not (lst[a].len==sa and lst[b].len==sb): return False
    return True
 
n,m = map(int,input().split())
lst = [trash(0,max_,0),trash((n+1)*2,max_,0)]
for _ in range(m):
    x,w,d = input().split()
    x,w = map(int,(x,w))
    p = -1 if d == 'L' else 1
 
    lst.append(trash(x*2,w,p))
 
lst.sort()

adj = [[i-1,i+1] for i in range(m+2)] #인접한 번호 기록
adj[0][0] = None
adj[-1][1] = None
 
v = [True]*(m+2) #유효한 더미 or 벽
 
heap = []
for i in range(1,m+2):
    update(i-1,i)

#글로벌 시간
time = 0
while True:
    while heap and not check(heap[0][2],heap[0][3]):
        heappop(heap)
        
    if not heap: break
    
    t,loc,idx,size = heappop(heap)
    while heap and not check(heap[0][2],heap[0][3]):
        heappop(heap)

    same = False
    if heap:
        t2,loc2,idx2,size2 = heap[0]
        if t == t2 and idx[1] == idx2[0]:
            same = True
            heappop(heap)
 
    time = t
 
    #충돌 처리
    if not same:
        a,b = idx
        merge2(t,loc,(a,b))
    else:
        a,b = idx
        _,c = idx2
        merge3(t,loc,(a,b,c))

    #다음 충돌 기록
    update(adj[a][0],a)
    update(a,adj[a][1])

res = (lst[0].len!=2) + sum(v[1:m+1])
print(f'{time/2:0.1f}',res)