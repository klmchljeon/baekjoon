a,b,c = input().split()

res = 3000
for i in '+-*/':
    ab = eval(a+i+b)
    if int(ab)!=ab: continue

    ab = str(int(ab))
    for j in '+-*/':
        p = eval(ab+j+c)
        
        if p >= 0 and int(p)==p:
            res = min(res,int(p))

print(res)