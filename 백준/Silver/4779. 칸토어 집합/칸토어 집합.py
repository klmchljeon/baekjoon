def f(s,e):
    if s==e:
        d[s] = '-'
        return 
    
    t = (e-s)//3
    f(s,s+t)
    f(e-t,e)
    return 

while True:
    try:
        n = int(input())
    except:
        break

    size = 3**n
    d = [' ']*size
    f(0,size-1)
    print(*d,sep = '')