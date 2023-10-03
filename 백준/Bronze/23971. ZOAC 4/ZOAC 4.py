h,w,n,m = map(int,input().split())

row = (h-1)//(n+1) + 1
col = (w-1)//(m+1) + 1

print(row*col)