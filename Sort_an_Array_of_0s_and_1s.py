n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if i==0:
        c+=1
for i in range(n):
    if i<c:
        print(0,end=" ")
    else:
        print(1,end=" ")