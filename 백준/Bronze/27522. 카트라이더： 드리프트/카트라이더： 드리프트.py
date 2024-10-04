#카트라이더: 드리프트
d = []
for _ in range(8):
    time,team = input().split()
    num = int(team == 'B')
    d.append(list(map(int,time.split(':')))+[num])

f = lambda x:(x[0],x[1],x[2])
d.sort(key = f)

score = [10,8,6,5,4,3,2,1,0]

tmp = [0,0]
for i,j in zip(d,score):
    tmp[i[3]] += j

res = tmp[0] > tmp[1]
print('Red' if res else 'Blue')