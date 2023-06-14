#컨베이어 벨트 위의 로봇
from collections import deque

def fir():
    up.appendleft(down.pop())
    down.appendleft(up.pop())
    
    robot.appendleft(0)
    robot.pop()

    if robot[n-1]:
        robot[n-1] = 0

    return 

def sec():
    for i in range(n-2,-1,-1):
        if not robot[i]: continue

        if not robot[i+1] and up[i+1]:
            up[i+1] -= 1
            robot[i] = 0
            robot[i+1] = 1

    if robot[n-1]:
        robot[n-1] = 0

    return 

def thi():
    if up[0]:
        up[0] -= 1
        robot[0] = 1

    return 

def check():
    cnt = 0
    for i in up+down:
        cnt += i==0

    return cnt >= k

n,k = map(int,input().split())
tmp = list(map(int,input().split()))

up = deque(tmp[:n])
down = deque(tmp[n:])
robot = deque([0]*n)

res = 1
while True:
    fir()
    sec()
    thi()
    if check():
        break

    res += 1

print(res)