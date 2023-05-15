#Cow Frisbee
n = int(input())
d = list(map(int,input().split()))

res = 0
stack = []
for i in range(n):
    while stack and stack[-1][0] < d[i]:
        idx = stack.pop()[1]
        res += i-idx+1

    if stack:
        res += i-stack[-1][1]+1

    stack.append((d[i],i))

print(res)