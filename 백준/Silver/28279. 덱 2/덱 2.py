import sys
from collections import deque
input = sys.stdin.readline

deq = deque([])
n = int(input())
for query in range(n):
    q,*ord = map(int,input().split())
    
    if q==1:
        deq.appendleft(ord[0])

    elif q==2:
        deq.append(ord[0])

    elif q==3:
        if deq:
            print(deq.popleft())
        else:
            print(-1)

    elif q==4:
        if deq:
            print(deq.pop())
        else:
            print(-1)

    elif q==5:
        print(len(deq))

    elif q==6:
        print(int(not bool(deq)))

    elif q==7:
        if deq:
            print(deq[0])
        else:
            print(-1)

    elif q==8:
        if deq:
            print(deq[-1])
        else:
            print(-1)