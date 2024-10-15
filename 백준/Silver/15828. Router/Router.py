import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([])
while True:
    m = int(input())
    if m == -1: break

    if m == 0:
        queue.popleft()
    elif len(queue) < n:
        queue.append(m)

print(*list(queue))