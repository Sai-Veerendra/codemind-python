def pal(num):
    sum=0
    while num>0:
        r=num%10
        sum=sum*10+r
        num=num//10
    return sum
n=int(input())
if n==pal(n): #pal(n)-->sum
    print("True")
else:
    print("False")