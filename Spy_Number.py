a=int(input())
s=0
pro=1
temp=0
while(a):
    temp=a%10
    pro*=temp
    s+=temp
    a//=10
if(s==pro):
    print("Spy Number")
else:
    print("Not Spy Number")