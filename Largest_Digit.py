n=int(input())
s=0
while(n!=0):
    a=n%10
    if s<a:
        s=a
    n//=10
print(s)