n = int(input())
lst = list(map(int,input().split()))
res = [[0,-1] for _ in range(n)]
stack = []
for i in range(n):
    while stack and stack[-1][0] <= lst[i]:
        stack.pop()

    if stack:
        res[i][0] += len(stack)
        res[i][1] = stack[-1][1]

    stack.append((lst[i],i+1))

stack = []
for i in range(n)[::-1]:
    while stack and stack[-1][0] <= lst[i]:
        stack.pop()

    if stack:
        res[i][0] += len(stack)
        if res[i][1] == -1 or (i+1)-res[i][1] > stack[-1][1]-(i+1):
            res[i][1] = stack[-1][1]

    stack.append((lst[i],i+1))

for i in res:
    if i[1] == -1:
        print(0)
    else:
        print(*i)