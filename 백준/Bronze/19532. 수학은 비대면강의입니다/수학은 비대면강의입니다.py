#수학은 비대면강의입니다
a,b,c,d,e,f = map(int,input().split())
for x in range(-999,1000):
    for y in range(-999,1000):
        con1 = a*x + b*y == c
        con2 = d*x + e*y == f

        if con1 and con2:
            print(x,y)
            exit()