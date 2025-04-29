import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
stack = [(-1,-1)]
res = 0
for i in range(n):
    while stack and stack[-1][0] >= lst[i]:
        h,idx = stack.pop()
        res = max(res,(i-stack[-1][1]-1)*h)

    res = max(res,(i-stack[-1][1])*lst[i])

    stack.append((lst[i],i))

while len(stack) > 1:
    h,idx = stack.pop()
    res = max(res,(n-stack[-1][1]-1)*h)

print(res)