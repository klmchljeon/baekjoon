n = input()[::-1]
flag = False
cnt = 0
for i in n:
    if i == '0' and flag:
        cnt += 1
    
    if i != '0':
        flag = True
        
print(cnt)