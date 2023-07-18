#RPG Extreme
import sys
input = sys.stdin.readline

def exe(event):
    global x,y
    global end_game
    if event == '^':
        if 'DX' in eq['O']:
            stat['hp'][0] -= 1
        else:
            stat['hp'][0] -= 5

        if stat['hp'][0] <= 0:
            stat['hp'][0] = 0

            if 'RE' in eq['O']:
                eq['O'].remove('RE')
                x,y = player_loc
                stat['hp'][0] = stat['hp'][1]
                return
            
            end_game = True
        return

    if event == 'B':
        open_box(box[(x,y)])
        return 

    if event == '&':
        end_game = fight(mob[(x,y)],False)
        return
    
    if event == 'M':
        lose = fight(mob[(x,y)],True)
        if RE:
            return
        if not lose:
            d[x] = d[x][:y]+'@'+d[x][y+1:]
        end_game = True
        return 

def open_box(item):
    d[x] = d[x][:y]+'.'+d[x][y+1:]
    t = item[0]
    if t == 'O':
        if len(eq[t]) < 4:
            eq[t].add(item[1])
    else:
        eq[t] = int(item[1])
    return

def fight(monster,boss):
    global x,y
    global RE
    mob_hp = monster[3]
    RE = False
    lose = False

    HU = 'HU' in eq['O']
    first_turn = True
    p_att = stat['att'] + eq['W']
    p_def = stat['def'] + eq['A']
    m_att = monster[1]
    m_def = monster[2]
    p_damage = max(1, m_att - p_def)
    m_damage = max(1, p_att - m_def)
    
    while True:
        if first_turn:
            first_turn = False
            patt = p_att
            matt = m_att

            if 'CO' in eq['O']:
                patt += p_att
                if 'DX' in eq['O']:
                    patt += p_att
            
            if boss and HU:
                stat['hp'][0] = stat['hp'][1]

            monster[3] -= max(1, patt - m_def)
            if monster[3] <= 0:
                break

            stat['hp'][0] -= max(1, matt - p_def) if not (HU and boss) else 0
            if stat['hp'][0] <= 0:
                stat['hp'][0] = 0
                lose = True
                break

        else:
            monster[3] -= m_damage
            if monster[3] <= 0:
                break

            stat['hp'][0] -= p_damage
            if stat['hp'][0] <= 0:
                stat['hp'][0] = 0
                lose = True
                break

    if not lose:
        d[x] = d[x][:y]+'.'+d[x][y+1:]

        if 'HR' in eq['O']:
            stat['hp'][0] = min(stat['hp'][0]+3, stat['hp'][1])

        exp = monster[4]
        if 'EX' in eq['O']:
            exp = int(1.2*exp)

        stat['exp'][0] += exp
        if stat['exp'][0] >= stat['exp'][1]:
            stat['lv'] += 1
            stat['exp'] = [0, 5*stat['lv']]
            
            stat['hp'] = [stat['hp'][1]+5]*2
            stat['att'] += 2
            stat['def'] += 2

    if lose and 'RE' in eq['O']:
        lose = False
        eq['O'].remove('RE')
        x,y = player_loc
        stat['hp'][0] = stat['hp'][1]
        monster[3] = mob_hp
        RE = True
    
    return lose

def print_result():
    if not end_game:
        d[x] = d[x][:y]+'@'+d[x][y+1:]
    for i in d:
        print(i)
    
    print(f'Passed Turns : {T}')
    print(f'LV : {stat["lv"]}')
    print(f'HP : {stat["hp"][0]}/{stat["hp"][1]}')
    print(f'ATT : {stat["att"]}+{eq["W"]}')
    print(f'DEF : {stat["def"]}+{eq["A"]}')
    print(f'EXP : {stat["exp"][0]}/{stat["exp"][1]}')
    if end_game:
        if stat['hp'][0] <= 0:
            stat['hp'][0] = 0
            if d[x][y] == '^':
                cause = 'SPIKE TRAP'
            else:
                cause = mob[(x,y)][0]
            print(f'YOU HAVE BEEN KILLED BY {cause}..')
        else:
            print('YOU WIN!')
    else:
        print('Press any key to continue.')

n,m = map(int,input().split())
d = [input().rstrip() for _ in range(n)]
mov = input().rstrip()

box_cnt = 0
mob_cnt = 0
for i in range(n):
    for j in range(m):
        a = d[i][j]
        if a == 'B':
            box_cnt += 1
        elif a == '&':
            mob_cnt += 1
        elif a == '@':
            player_loc = [i,j]
            d[i] = d[i][:j]+'.'+d[i][j+1:]
        elif a == 'M':
            mob_cnt += 1

mob = dict()
box = dict()
for _ in range(mob_cnt):
    r,c,*inf = input().split()
    r,c = map(int,(r,c))
    inf[1:] = map(int,inf[1:])
    mob[(r-1,c-1)] = inf

for _ in range(box_cnt):
    r,c,*inf = input().split()
    r,c = map(int,(r,c))
    box[(r-1,c-1)] = inf

dx = {'L':0, 'R':0, 'U':-1, 'D':1}
dy = {'L':-1, 'R':1, 'U':0, 'D':0}

x,y = player_loc
stat = {'lv':1, 'hp':[20,20], 'att':2, 'def':2, 'exp':[0,5]}
eq = {'W':0, 'A':0, 'O':set()}
end_game = False
T = 0
for i in mov:
    T += 1
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<m and d[nx][ny] != '#':
        x = nx
        y = ny
    
    exe(d[x][y])
    if end_game:
        break

print_result()
