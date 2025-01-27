n = int(input())
lst = list(map(int,input().split()))
stack = []
res = 0
for i in lst:
    while stack and stack[-1] > i:
        stack.pop()

    if stack:
        res = max(res,i-stack[0])

    stack.append(i)

print(res)