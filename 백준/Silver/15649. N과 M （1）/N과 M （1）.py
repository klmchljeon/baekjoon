def bt(leng):
    #leng == 목표 수열의 길이
    if len(s) == leng:
        print(*s)
        return 
    
    #트리의 선택지를 살펴봄
    for i in range(1,n+1):
        #선택할 수 있는 선택지임?
        if not i in s:
            s.append(i) #선택
            bt(leng)
            s.pop() #돌아오기

n,m = map(int,input().split())

s = [] #현재 내가 선택한 노드들(==지금까지 만든 수열)
bt(m)