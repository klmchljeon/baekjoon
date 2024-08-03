def check(lst):
    return len(set(lst)) == m

def bf():
    if len(s) == m:
        if check(s):
            print(*s)
        
        return 

    for i in range(1,n+1):
        s.append(i)
        bf()
        s.pop()

n,m = map(int,input().split())

s = []
bf()