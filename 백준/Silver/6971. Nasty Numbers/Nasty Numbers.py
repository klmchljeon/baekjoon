t = int(input())
for case in range(t):
    n = int(input())
    lst = []
    for i in range(1,int(n**0.5)+1):
        if n%i==0 and i**2!=n:
            lst.append((i,n//i))

    flag = False
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            a,b = lst[i]
            c,d = lst[j]
            if abs(a-b)==c+d or abs(c-d)==a+b:
                flag = True
                break

    if flag:
        print(f'{n} is nasty')
    else:
        print(f'{n} is not nasty')