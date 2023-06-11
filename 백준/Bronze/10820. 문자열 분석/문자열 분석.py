#문자열 분석
while True:
    try: 
        st = input()
    except: 
        break
    
    cnt = [0]*4
    
    for i in st:
        if 'a' <= i <= 'z':
            cnt[0] += 1

        elif 'A' <= i <= 'Z':
            cnt[1] += 1
        
        elif '0' <= i <= '9':
            cnt[2] += 1

        else:
            cnt[3] += 1

    print(*cnt)