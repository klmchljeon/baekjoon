max_ = 100000

g = int(input())

flag = True

e = 1 #현재 몸무게
for s in range(1,max_+1): #기억하던 몸무게
    while e**2 - s**2 < g:
        e += 1

    if e**2 - s**2 == g:
        print(e)
        flag = False

if flag: print(-1)