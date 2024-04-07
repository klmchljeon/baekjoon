#오등큰수
max_ = 1000000
n = int(input())
d = list(map(int,input().split()))

cnt = [0]*(max_+1)
for i in d:
    cnt[i] += 1

ngf = []

stack = []
for i in d[::-1]:
    while stack and stack[-1][1]<=cnt[i]:
        stack.pop()

    if not stack:
        ngf.append(-1)
    else:
        ngf.append(stack[-1][0])
    
    stack.append((i,cnt[i]))

print(*ngf[::-1])