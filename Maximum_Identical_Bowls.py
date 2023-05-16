n=int(input())
l=list(map(int,input().split()))
while(n):
    if sum(l)%n==0:
        print(n)
        break
    else:
        n-=1