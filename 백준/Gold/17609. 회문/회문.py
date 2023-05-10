#회문
def check(string,start,end):
    s,e = start,end
    while s<=e:
        if string[s] == string[e]:
            s += 1
            e -= 1

        else: break
    
    return string,s,e

t = int(input())
for case in range(t):
    st = input()
    s,e = 0,len(st)-1
    st,s,e = check(st,s,e)
    if s<=e:
        if st[s+1] == st[e]:
            _,ls,le = check(st,s+1,e)
            if ls > le:
                print(1)
                continue

        if st[s] == st[e-1]:
            _,rs,re = check(st,s,e-1)
            if rs > re:
                print(1)
                continue

        print(2)
    else:
        print(0)