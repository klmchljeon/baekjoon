import sys
input = sys.stdin.readline

II,NN,UU = 'II','NN','UU'
IN,IU,NU = 'IN','IU','NU'

dic = dict()
for i in (II,NN,UU,IN,IU,NU):
    dic[i] = [0,0,1001]

n = int(input())
for _ in range(n):
    a,t = input().split()
    if a[0] > a[1]:
        a = a[1]+a[0]
    t = int(t)

    dic[a][0] += 1
    dic[a][1] += t
    dic[a][2] = min(dic[a][2],t)

res = 0
#끝이 다른 막대기 없이 
res = max(res, dic[II][1], dic[NN][1], dic[UU][1])

#끝이 다른 막대기 1종 
if dic[IN][0]>0:
    tmp = dic[II][1] + dic[IN][1] + dic[NN][1]
    res = max(res,tmp)

if dic[IU][0]>0:
    tmp = dic[II][1] + dic[IU][1] + dic[UU][1]
    res = max(res,tmp)

if dic[NU][0]>0:
    tmp = dic[NN][1] + dic[NU][1] + dic[UU][1]
    res = max(res,tmp)

#끝이 다른 막대기 2종
if dic[IN][0]>0 and dic[IU][0]>0:
    tmp = dic[NN][1] + dic[IN][1] + dic[II][1] + dic[IU][1] + dic[UU][1]
    res = max(res,tmp)

if dic[IN][0]>0 and dic[NU][0]>0:
    tmp = dic[II][1] + dic[IN][1] + dic[NN][1] + dic[NU][1] + dic[UU][1]
    res = max(res,tmp)

if dic[NU][0]>0 and dic[IU][0]>0:
    tmp = dic[NN][1] + dic[NU][1] + dic[UU][1] + dic[IU][1] + dic[II][1]
    res = max(res,tmp)

#끝이 다른 막대기 3종
if dic[IN][0]>0 and dic[IU][0]>0 and dic[NU][0]>0:
    tmp = dic[NN][1] + dic[IN][1] + dic[II][1] + dic[IU][1] + dic[UU][1] + dic[NU][1]
    
    #홀수가 하나도 없다면
    '''if dic[IN][0]%2==0 and dic[IU][0]%2==0 and dic[NU][0]%2==0:
        raise ValueError
        tmp -= min(dic[IN][2],dic[IU][2],dic[NU][2])'''

    res = max(res,tmp)

print(res)