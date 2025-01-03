def conv(st):
    return tuple(map(int,st.split(':')))

def convr(time):
    a,b = time
    return f'{a:02d}:{b:02d}'

def prev(time):
    a,b = time
    b -= 10
    if b < 0:
        b += 60
        a -= 1
        
    if a < 0:
        a = 0
        b = 0
        
    return (a,b)

def next_(time,m):
    a,b = time
    b += 10
    if b >= 60:
        b -= 60
        a += 1
        
    if not le_eq((a,b),m):
        return m
    
    return (a,b)
        
def le_eq(a,b):
    if a[0] != b[0]:
        return a[0] < b[0]
    return a[1] <= b[1]

def skip(s,e,time):
    if le_eq(s,time) and le_eq(time,e):
        return e
    
    return time

def solution(video_len, pos, op_start, op_end, commands):
    max_ = conv(video_len)
    cur = conv(pos)
    s,e = conv(op_start),conv(op_end)
    
    cur = skip(s,e,cur)
    for c in commands:
        if c == "next":
            cur = next_(cur,max_)
        else:
            cur = prev(cur)
        cur = skip(s,e,cur)
            
    
    return convr(cur)