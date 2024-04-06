l,k = map(int,input().split())
arr = sorted(list(map(int,input().split())))
if k == 0:
    ans = arr[0]-1
else:
    ans = arr[k-1]
cnt = 0
for i in arr:
    if i <=ans:
        cnt+=1
print(-1 if ans<1 or cnt!=k else ans)
