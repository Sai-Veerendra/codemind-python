n=int(input())
arr=list(map(int,input().split()))
maxsub=arr[0]
cursum=0
for i in arr:
    if cursum<0:
        cursum=0
    cursum+=i
    maxsub=max(maxsub,cursum)
print(maxsub)