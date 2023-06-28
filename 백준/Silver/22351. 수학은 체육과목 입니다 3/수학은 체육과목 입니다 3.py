def check(sol):
    tmp = int(sol)

    lens = len(sol)
    idx = len(sol)
    while idx < n:
        tmp += 1
        if tmp in (10,100):
            lens += 1

        if tmp != int(st[idx:idx+lens]):
            return False
        
        idx += lens

    return sol,tmp

st = input()
n = len(st)

for i in range(1,4):
    a = check(st[:i])
    if a != False:
        print(*a)
        exit()