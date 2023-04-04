n=int(input())
arr=list(map(int,input().split()))
brr=[]
for i in range(n):
    if arr[i]==0:
        brr.append(arr[i])
for j in range(n):
    if arr[j]==1:
        brr.append(arr[j])
print(*brr)