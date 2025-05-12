from collections import deque

n = int(input())
queue = deque([n])
for i in range(1,n)[::-1]:
    queue.appendleft(i)
    for j in range(i):
        queue.appendleft(queue.pop())

print(*list(queue))