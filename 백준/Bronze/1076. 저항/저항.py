#저항
lst = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
dic = dict(zip(lst,range(10)))

a,b,c = [input() for _ in range(3)]

res = int(str(dic[a])+str(dic[b]))*(10**dic[c])
print(res)