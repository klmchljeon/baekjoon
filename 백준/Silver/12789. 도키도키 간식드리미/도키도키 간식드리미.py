n = int(input())
d = list(map(int,input().split()))

stack = []

x = 1
for i in d:
    if i != x:
        while stack and stack[-1] == x:
            stack.pop()
            x += 1

        else:
            stack.append(i)
    
    else:
        x += 1

while stack:
    if x == stack[-1]:
        stack.pop()
        x += 1
    else:
        print('Sad')
        break

else:
    print('Nice')