import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    x,r = map(int,input().split())
    lst.append((x-r,-r,i))
    lst.append((x+r,r,i))

lst.sort()
for i in range(len(lst)-1):
    if lst[i][0] == lst[i+1][0]:
        print('NO')
        exit()

stack = []
for a,p,i in lst:
    if p < 0:
        stack.append(i)
    else:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            print('NO')
            break

else:
    print('YES')