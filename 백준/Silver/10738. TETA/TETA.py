k = int(input())
lst = [0] + list(map(int,input().split()))
x = int(input())
menu = list(map(int,input().split()))
t = int(input())
meals = list(map(int,input().split()))

dic = dict()
for i in meals:
    if not i in dic:
        dic[i] = 0

    dic[i] += 1

res = sum([lst[i]*dic[i] for i in dic])
cnt = 1
while True:
    tmp = x*cnt

    flag = True
    for i in menu:
        if i in dic:
            dic[i] -= 1
            flag = False

            if dic[i] == 0:
                del dic[i]

    if flag:
        break

    tmp += sum([lst[i]*dic[i] for i in dic])
    res = min(res,tmp)
    cnt += 1

print(res)