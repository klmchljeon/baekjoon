#부등호
def ins(num):
    if res[0] < num:
        res[0] = num[:]

    if res[1] > num:
        res[1] = num[:]

    return 

def cal(lst):
    for i in range(n):
        if st[i]=='<' and lst[i]>lst[i+1]:
            return 0

        elif st[i]=='>' and lst[i]<lst[i+1]:
            return 0
        
    return 1

def dfs():
    if len(s) == n+1:
        if cal(s):
            ins(s)
        return 

    for i in range(10):
        if not i in s:
            s.append(i)
            dfs()
            s.pop()

    return 

n = int(input())
st = input().split()

s = []
res = [[0]*(n+1),[9]*(n+1)]
dfs()

for i in res:
    print(''.join(map(str,i)))