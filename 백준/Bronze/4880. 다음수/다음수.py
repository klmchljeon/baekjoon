#다음수
while True:
    a,b,c = map(int,input().split())
    if not (a or b or c): break

    if b-a == c-b:
        tmp = c-b
        print('AP',c+tmp)

    else:
        tmp = c//b
        print('GP',c*tmp)