#숫자 야구
def check(num):
    for q,s,b in d:
        x,y = 0,0
        for i in range(3):
            if q[i] == num[i]:
                x += 1
            elif q[i] in num:
                y += 1

        flag = s==x and b==y
        if not flag:
            return False
        
    return True

def dfs():
    if len(s) == 3:
        lst.append(s[:])
        return 
    
    for i in range(1,10):
        if not i in s:
            s.append(i)
            dfs()
            s.pop()

    return 

n = int(input())
d = []
for i in range(n):
    a,b,c = input().split()
    b,c = map(int,(b,c))
    d.append((list(map(int,a)),b,c))

lst = []
s = []
dfs()

res = 0
for i in lst:
    res += check(i)

print(res)