a = 'acijnotvw'
b = ['@','[','!',';','^','0','7','\\\'','\\\\\'']
dic = dict(zip(b,a))

t = int(input())
for case in range(t):
    lst = list(input())
    n = len(lst)

    cnt = 0
    res = []
    while lst:
        for l in range(3,0,-1):
            tmp = ''.join(lst[-l:])
            if tmp in dic:
                res.append(dic[tmp])
                del lst[-l:]
                
                cnt += 1
                break

        else:
            res.append(lst[-1])
            del lst[-1]

    h = len(res)//2 + len(res)%2
    if cnt < h:
        print(''.join(res[::-1]))
    else:
        print('I don\'t understand')