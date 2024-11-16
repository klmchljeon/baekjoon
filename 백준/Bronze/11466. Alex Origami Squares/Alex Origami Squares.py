h,w = map(int,input().split())
if h > w:
    h,w = w,h

a = min(h,w/3)
b = min(h/2,w/2)
print(max(a,b))