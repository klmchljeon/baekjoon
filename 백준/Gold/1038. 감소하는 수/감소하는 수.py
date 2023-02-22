#감소하는 수

#9876543210 -> 10자리까지만 구하면 됨
import sys
input = sys.stdin.readline

def dfs(init):
    global s

    if len(s) == init+1:
        d.append(s[1:])

    else:
        for i in range(10):
            if s[-1]>i:
                s.append(i)
                dfs(init)
                s.pop()
d = []
s = [10]
for i in range(1,11):
    dfs(i)

n = int(input())
if n>=len(d): 
    print(-1)
else:
    print(''.join(map(str,d[n])))