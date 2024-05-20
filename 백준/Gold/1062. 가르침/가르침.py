#가르침
def dfs():
    global res
    if len(s) == k-5:
        res = max(res, cal(s))
        return 

    for i in range(26):
        if i in base: continue
        
        if not s or s[-1] < i:
            s.append(i)
            dfs()
            s.pop()

def cal(lst):
    t = 0b10000010000100000101
    for i in lst:
        t |= 0b1 << i
    
    cnt = 0
    for i in d:
        if t|i == t:
            cnt += 1

    return cnt

n,k = map(int,input().split())
d = []
for _ in range(n):
    st = input()
    b = 0b0
    for i in st:
        b |= 0b1 << (ord(i)-ord('a'))

    d.append(b)

if k < 5: 
    print(0)
    exit()

base = set([0,2,8,13,19])
res = 0
s = []
dfs()
print(res)