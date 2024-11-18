class book:
    def __init__(self,n,a,t):
        self.n = n
        self.a = a
        self.t = t

    def query_n(self,n):
        return self.n == n
    
    def query_ni(self,n):
        return n in self.n
    
    def query_a(self,a):
        return self.a == a
    
    def query_t(self,t):
        return t in self.t
    
    def query(self,st):
        m,s = st.split(':')
        if m == 'n':
            return self.query_n(s)
        
        if m == 'ni':
            return self.query_ni(s)
        
        if m == 'a':
            return self.query_a(s)
        
        if m == 't':
            return self.query_t(s)

def cal(mode,idx,b):
    lst = []
    tmp = ''
    while idx < len(st):
        if st[idx] in ', ':
            if tmp:
                lst.append(b.query(tmp))
                tmp = ''

            idx += 1
            continue

        if st[idx] in 'OAN':
            if idx == 0 or st[idx-1] in '( ':
                p,i = cal(st[idx],idx+2,b)
                lst.append(p)
                idx = i+1

        if idx >= len(st) or st[idx] == ')':
            break

        if not st[idx] in ', )':
            tmp += st[idx]

        idx += 1

    if tmp:
        lst.append(b.query(tmp))
        tmp = ''

    if mode == 'A':
        return all(lst),idx
    
    if mode == 'O':
        return any(lst),idx
    
    if mode == 'N':
        return not lst[0],idx

n = int(input())
lst = []
for _ in range(n):
    name,author,*tags = input().split()
    lst.append(book(name,author,set(tags)))

m = int(input())
for _ in range(m):
    st = input()
    cnt = 0
    for i in lst:
        cnt += cal('A',0,i)[0]

    print(cnt)