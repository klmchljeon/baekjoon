n,k = map(int,input().split())
d = list(map(int,input()))

stack = []
for i in d:
    while stack and k and stack[-1] < i:
        stack.pop()
        k-=1

    stack.append(i)

while k:
    stack.pop()
    k-=1

print(''.join(map(str,stack)))