import sys
from collections import deque
sys.setrecursionlimit(int(1e5))

class Random:
    def __init__(self,seed:str):
        lst = []
        for i in ''.join(seed.split('-')):
            if '0' <= i <= '9':
                lst.append(int(i))

            else:
                lst.append(ord(i)-ord('A')+10)

        lst = lst[::-1]
        res = 0
        for i in range(len(lst)):
            res += lst[i]*(36**i)

        self.s = res % (2**31)
        self.cnt = 0

    def rand(self) -> int:
        a = 1103515245
        c = 12345
        m = 2**31

        res = self.s

        self.s = (a*self.s + c)%m
        self.cnt += 1
        return res

    def randint(self,l,r) -> int:
        return l + self.rand()%(r-l+1)

    def chance(self,p) -> bool:
        return self.randint(1,100) <= p

    def choice(self,arr):
        return arr[self.randint(0,len(arr)-1)]

class Dungeon:
    def __init__(self,r:Random):
        self.random = r
        self.x = [4,4]
        self.y = [4,4]

        self.step1()
        self.step2()
        self.step3()

    def cal(self,loc):
        x,y = loc
        self.x = [min(self.x[0],x),max(self.x[1],x)]
        self.y = [min(self.y[0],y),max(self.y[1],y)]

    def step1(self):
        self.n = self.random.randint(10,20)

    def step2(self):
        dx = (0,1,0,-1)
        dy = (1,0,-1,0)

        def check(loc):
            x,y = loc
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0<=nx<self.size and 0<=ny<self.size): continue

                cnt += self.board[nx][ny] != None

            return cnt >= 2

        self.size = 9
        cnt = 0

        self.board = [[None]*self.size for _ in range(self.size)]
        self.room = []
        
        self.room.append((4,4))
        self.board[4][4] = 'R'

        while cnt < self.n:
            queue = deque([self.random.choice(self.room)])
            while queue and cnt < self.n:
                x,y = queue.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if cnt == self.n: break
                    if not (0<=nx<self.size and 0<=ny<self.size): continue
                    if self.board[nx][ny] != None: continue
                    if check((nx,ny)): continue
                    if self.random.chance(50) == False: continue

                    self.board[nx][ny] = 0
                    self.room.append((nx,ny))
                    self.cal((nx,ny))

                    queue.append((nx,ny))
                    cnt += 1

        self.room.remove((4,4))

    def step3(self):
        dx = (0,0,1,-1)
        dy = (1,-1,0,0)

        self.special = []
        #st = set(self.room)

        #스페셜 방 지정
        for x,y in self.room:
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0<=nx<self.size and 0<=ny<self.size): continue
                cnt += self.board[nx][ny] != None

            if cnt != 1: continue

            self.board[x][y] = -1
            self.special.append((x,y))

        require = []
        for i in range(10):
            require.extend([i]*(10-i))

        #일반방 요구 공격력 지정
        for x,y in self.room:
            if self.board[x][y] != -1:
                self.board[x][y] = self.random.choice(require)

        #보스방 지정
        boss = []
        for x,y in self.special:
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                cnt += (nx,ny)==(4,4)

            if cnt: continue
            boss.append((x,y))

        boss_room = self.random.choice(boss)
        x,y = boss_room
        self.board[x][y] = 'B'

        self.special.remove(boss_room)

        #비밀방 지정
        if self.special:
            secret_room = self.random.choice(self.special)
            x,y = secret_room
            self.board[x][y] = 'X'

            self.special.remove(secret_room)

        #보물방 지정
        if self.special:
            treasure_room = self.random.choice(self.special)
            x,y = treasure_room
            self.board[x][y] = 'T'

            self.special.remove(treasure_room)


        #추가 보물방 지정
        if self.n >= 15 and self.special:
            if self.random.chance(25) == True:
                treasure_room2 = self.random.choice(self.special)
                x,y = treasure_room2
                self.board[x][y] = 'T'

                self.special.remove(treasure_room2)

        #상점방 지정
        if self.special:
            if self.n <= 15 or self.random.chance(66) == True:
                store_room = self.random.choice(self.special)
                x,y = store_room
                self.board[x][y] = 'M'

                self.special.remove(store_room)

        #악마방/천사방 생성
        devil_room = None
        angel_room = None
        if self.random.chance(20) == True:
            reward = []
            x,y = boss_room
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                xm,xM = self.x
                ym,yM = self.y
                if not (xm<=nx<=xM and ym<=ny<=yM): continue
                if self.board[nx][ny] != None: continue

                reward.append((nx,ny))

            if reward:
                tmp = self.random.choice(reward)
                if self.random.chance(50) == True:
                    devil_room = tmp
                    x,y = devil_room
                    self.board[x][y] = 'D'

                else:
                    angel_room = tmp
                    x,y = angel_room
                    self.board[x][y] = 'A'

        #희생방 지정
        if self.special:
            if angel_room != None or self.random.chance(14) == True:
                sacrifice_room = self.random.choice(self.special)
                x,y = sacrifice_room
                self.board[x][y] = 'S'

                self.special.remove(sacrifice_room)

        #저주방 지정
        if self.special:
            if devil_room != None and self.random.chance(50) == True:
                curse_room = self.random.choice(self.special)
                x,y = curse_room
                self.board[x][y] = 'C'

                self.special.remove(curse_room)

        #일반방 추가 지정
        for x,y in self.special:
            self.board[x][y] = self.random.choice(require)

    def printf(self):
        h = self.x[1]-self.x[0]+1
        w = self.y[1]-self.y[0]+1

        n = 6*h + 3
        m = 6*w + 3
        lst = [[' ']*m for _ in range(n)]
        for i in (0,n-1):
            for j in range(m):
                lst[i][j] = '#'

        for j in (0,m-1):
            for i in range(n):
                lst[i][j] = '#'

        ver = [(-2,-2),(-2,2),(2,2),(2,-2)]
        hside = [(-2,-1),(-2,0),(-2,1),(2,-1),(2,0),(2,1)]
        vside = [(-1,-2),(0,-2),(1,-2),(-1,2),(0,2),(1,2)]

        dx = (-1,0,1,0)
        dy = (0,-1,0,1)

        x = self.x[0]
        for i in range(4,n-3,6):
            y = self.y[0]
            for j in range(4,m-3,6):
                if self.board[x][y] != None:
                    lst[i][j] = str(self.board[x][y])

                    flag = False
                    flag2 = self.board[x][y] == 'X'
                    if self.board[x][y] == 'B' or self.board[x][y] == 'R':
                        for di,dj in ver+hside+vside:
                            ni = i + di
                            nj = j + dj
                            lst[ni][nj] = '@'

                    elif self.board[x][y] == 'D' or self.board[x][y] == 'A':
                        flag2 = True
                        cnt = 0
                        for di,dj in ver:
                            ni = i + di
                            nj = j + dj
                            lst[ni][nj] = '/' if cnt%2==0 else '\\'
                            cnt += 1

                        cnt = 0
                        for di,dj in hside:
                            ni = i + di
                            nj = j + dj
                            lst[ni][nj] = '^' if cnt<3 else 'v'
                            cnt += 1

                        cnt = 0
                        for di,dj in vside:
                            ni = i + di
                            nj = j + dj
                            lst[ni][nj] = '<' if cnt<3 else '>'
                            cnt += 1
                    
                    else:
                        flag = True
                        for di,dj in ver:
                            ni = i + di
                            nj = j + dj
                            lst[ni][nj] = '+'

                        for di,dj in hside:
                            ni = i + di
                            nj = j + dj
                            lst[ni][nj] = '-'

                        for di,dj in vside:
                            ni = i + di
                            nj = j + dj
                            lst[ni][nj] = '|'

                    if flag2:
                        y += 1
                        continue
                    for k in range(4):

                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if not (0<=nx<self.size and 0<=ny<self.size): continue
                        if self.board[nx][ny] != None and self.board[nx][ny] != 'D' and self.board[nx][ny] != 'A' and self.board[nx][ny] != 'X':
                            ni = i + dx[k]*2
                            nj = j + dy[k]*2
                            lst[ni][nj] = ' '

                            nni = i + dx[k]*3
                            nnj = j + dy[k]*3
                            for kk in ((k+1)%4,(k+3)%4):
                                nnni = nni + dx[kk]
                                nnnj = nnj + dy[kk]
                                lst[nnni][nnnj] = '|' if k%2==0 else '-'

                                if flag:
                                    nnni = ni + dx[kk]
                                    nnnj = nj + dy[kk]
                                    lst[nnni][nnnj] = '+'

                y += 1

            x += 1


        for i in lst:
            print(''.join(i))

seed = input()
r = Random(seed)
d = Dungeon(r)

room = []
idx = dict()
for i in range(9):
    for j in range(9):
        if d.board[i][j] != None:
            room.append((i,j))
            idx[(i,j)] = len(idx)

dx = (-1,1,0,0)
dy = (0,0,-1,1)

adj = []
for x,y in room:
    tmp = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<9 and 0<=ny<9): continue
        if d.board[nx][ny] != None:
            tmp.append((nx,ny))

    adj.append(tmp)

n = len(room)
start = idx[(4,4)]

st = set()
p = (6,1,0,3,1<<start,False)
st.add(p)

res = False
def bt(p):
    global res
    if res: return
    h,a,c,b,state,m = p

    tmp = []
    for i in range(n):
        if not state&(1<<i): continue
        
        for x,y in adj[i]:
            if state&(1<<idx[(x,y)]): continue

            t = d.board[x][y]
            #보물방 
            if t == 'T':
                a += 1
                state |= 1<<idx[(x,y)]

            #비밀방
            elif t == 'X' and b:
                h += 2
                a += 2
                c += 2
                b -= 1
                state |= 1<<idx[(x,y)]

            #상점방
            elif t == 'M':
                m = True
                state |= 1<<idx[(x,y)]

            #일반방
            elif type(t) == type(1):
                #바로 가도 됨
                if t <= a:
                    c += 1
                    state |= 1<<idx[(x,y)]

                #바로 통과 못함
                else:
                    tmp.append((x,y))

            #희생방, 저주방
            elif t != 'B':
                tmp.append((x,y))

    if m:
        if (10-a)*2 <= c:
            res = True
            return 
    
        cnt = c//2
        for i in range(cnt+1):
            np = (h+i,a+(cnt-i),c%2,b,state,m)
            if not np in st:
                st.add(np)
                bt(np)
    
    np = (h,a,c,b,state,m)
    if not np in st:
        st.add(np)
        bt(np)

    for x,y in tmp:
        t = d.board[x][y]
        #어려운 일반방
        if type(t) == type(1):
            #체력으로 입장
            if h > 1:
                np = (h-1,a,c+1,b,state|(1<<idx[(x,y)]),m)
                if not np in st:
                    st.add(np)
                    bt(np)

            #폭탄으로 입장
            if b:
                np = (h,a,c+1,b-1,state|(1<<idx[(x,y)]),m)
                if not np in st:
                    st.add(np)
                    bt(np)

        #희생방
        elif t == 'S' and h > 2:
            np = (h-2,a+3,c,b,state|(1<<idx[(x,y)]),m)
            if not np in st:
                st.add(np)
                bt(np)

        #저주방
        elif t == 'C':
            np = (h,a-2,c+3,b+1,state|(1<<idx[(x,y)]),m)
            if not np in st:
                st.add(np)
                bt(np)

bt(p)

print('CLEAR' if res else 'GAME OVER')
d.printf()