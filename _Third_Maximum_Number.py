n=int(input())
arr=list(map(int,input().split()))
arr.sort()
r=0
for i in range(n-2):
    r=arr[i]
if n-3>=0:
    print(r)
else:
    print(max(arr))