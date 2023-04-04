n=int(input())
arr=list(map(int,input().split()))
l=0
for i in range(n):
    if arr[i]:
        arr[l],arr[i]=arr[i],arr[l]
        l+=1
print(*arr)