def find(m,idx):
    leng = idx+2
    if 0 < m <= d[idx-1]:
        return find(m,idx-1)
    
    if d[idx-1] < m <= d[idx-1]+leng:
        return 'm' if d[idx-1]+1==m else 'o'
    
    if d[idx-1]+leng < m <= d[idx]:
        return find(m-(d[idx-1]+leng),idx-1)

n = int(input())

d = [0,3]
while d[-1] < n:
    d.append(d[-1]*2 + len(d)+2)

print(find(n,len(d)-1))