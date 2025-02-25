n,h,w = map(int,input().split())
print(max(h,n-h)*max(w,n-w)*4)